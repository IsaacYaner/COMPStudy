// npm i ganache-time-traveler
// https://www.npmjs.com/package/ganache-time-traveler
const Auction = artifacts.require("Auction");
const Registry = artifacts.require("SophisticatedInvestorCertificateAuthorityRegistry");
const timeMachine = require('ganache-time-traveler');
const NeverPayShares = artifacts.require("NeverPayShares");
const { assertRevert } = require('./helpers/assertRevert');
const Web3EthAccounts = require('web3-eth-accounts');
const abi = require('web3-eth-abi');
const utils = require('web3-utils');

/*
  HELPER FUNCTIONS:
    ALL the same as the functions in the script.
*/
// Helper function called by sign()
function getSignHash(addr, message, year)
{
  const encoded = abi.encodeParameters(['address','string', 'uint256'],[addr, message, year]);
  const orderHash = utils.soliditySha3(encoded);
  return orderHash;
}

// Helper function for signing contract
function sign(addr, privateKey, account)
{
  message = 'The owner of Ethereum address '+addr+' is a sophisticated investor for year 2022.';
  hashi = getSignHash(addr, message, 2022);
  data = account.sign(hashi, privateKey);
  return data['signature']
}

// Helper function for getting order hash
function getHash(numShares, price, addr, nonce)
{
  const encoded = web3.eth.abi.encodeParameters(['uint256','uint256','uint256','address'],[numShares,price, nonce, addr]);
  const orderHash = web3.utils.soliditySha3(encoded);
  return orderHash;
}

// Time stamp for deadline of round 1
const timeRound1 = 1650412800;
// Time stamp for deadline of round 2
const timeRound2 = 1651017600;

contract('Auction', (accounts) => {
  let AuctionInstance;
  let signature
  let Shares;
  let Acc;
  let account;
  let basePrice = web3.utils.toBN(String("1000000000000000000"));
  let baseEther = 1;

  // Take a copy of the initial state
  beforeEach(async() => {
    let snapshot = await timeMachine.takeSnapshot();
    snapshotId = snapshot['result'];
  });

  // Recover to the initial state
  afterEach(async() => {
    await timeMachine.revertToSnapshot(snapshotId);
  });

  before('Deploy Contracts', async() => {
    // Create a institution to issue certificates
    account = await new Web3EthAccounts('ws://localhost:8546');
    Acc = await account.create();
    // ASIC registry
    RegistryInstance = await Registry.new({from: accounts[0]});
    // Auction instance
    AuctionInstance = await Auction.new(RegistryInstance.address, {from: accounts[0]});
    // Get address of ERC shares
    sharesAddress = await AuctionInstance.shares.call();
    // Get the contract located at the address
    Shares = await NeverPayShares.at(sharesAddress);

    // Authorise a certificate issuer
    await RegistryInstance.authorise(Acc['address']);    
    // Issue to account 0 - 6
    for (i = 0; i < 6; i++)
    {
      signature = await sign(accounts[i], Acc.privateKey, account);
      message = 'The owner of Ethereum address '+accounts[i]+' is a sophisticated investor for year 2022.';
      await AuctionInstance.verify(Acc['address'], message, signature, {from: accounts[i]});
    }

  });

  it('Correct Hash', async () => {
    // Check that the hash generated off-chain is the same as the hash of the contract.
    const orderHash = getHash(5,5,accounts[1],1);
    const hashValue = await AuctionInstance.hash(5,5, accounts[1], 1);
    assert.equal(orderHash, hashValue, "Generated hash is not correct");
  });

  it('Round 1 deadline and authorised', async () => {
    await timeMachine.advanceBlockAndSetTime(timeRound1-1000000);
    orderHash = getHash(5,5,accounts[1],1);
    
    //Reverted because not authorised as sophis/inv.
    await assertRevert(AuctionInstance.submitCommitment(orderHash, {from: accounts[7]}));
    await AuctionInstance.submitCommitment(orderHash, {from: accounts[1]});
    
    // Too late to submit
    await timeMachine.advanceBlockAndSetTime(timeRound1+1000000);
    orderHash = getHash(5,5,accounts[1],1);
    await assertRevert(AuctionInstance.submitCommitment(orderHash, {from: accounts[1]}));
  });
  it('Round 2 appropriate time', async () => {
    price = basePrice;
    amount = 5;
    fee = price*amount;
    nonce = 1;

    // Set time to round 1
    // Suceed in submitting, but too early to open
    await timeMachine.advanceBlockAndSetTime(timeRound1-1000000);
    orderHash = getHash(amount, price,accounts[1],nonce);
    await AuctionInstance.submitCommitment(orderHash, {from: accounts[1]});
    await assertRevert(AuctionInstance.openCommitment(orderHash, amount, price, nonce, {from: accounts[1], value: fee}));

    // Set time to round 2
    // Can open
    await timeMachine.advanceBlockAndSetTime(timeRound1+100);
    orderHash = getHash(amount,price,accounts[1],nonce);
    await AuctionInstance.openCommitment(orderHash, amount, price, nonce, {from: accounts[1], value: fee});

    // After deadline of round 2
    // Too late to open
    await timeMachine.advanceBlockAndSetTime(timeRound2+1000000);
    orderHash = getHash(500,basePrice,accounts[1],1);
    await assertRevert(AuctionInstance.openCommitment(orderHash, amount, price, nonce, {from: accounts[1], value: fee}));
  });
  it('Round 2 other failing cases', async () => {
    price = basePrice;
    amount = 5;
    fee = price*amount;
    nonce = 1;
    
    // Set time to round 1 and submit the order
    await timeMachine.advanceBlockAndSetTime(timeRound1-1000000);
    orderHash = getHash(amount,price,accounts[1],nonce);
    await AuctionInstance.submitCommitment(orderHash, {from: accounts[1]});

    // Set time to round 2
    await timeMachine.advanceBlockAndSetTime(timeRound1+100);
    nonce += 1;
    orderHash = getHash(amount,price,accounts[1],nonce);
    // Order hash doesn't exist
    // Because the nonce is incorrect
    await assertRevert(AuctionInstance.openCommitment(orderHash, amount, price, nonce, {from: accounts[1], value: fee}));
    
    // Wrong order hash: incorrect amount entered
    await timeMachine.advanceBlockAndSetTime(timeRound1-100);
    await AuctionInstance.submitCommitment(orderHash, {from: accounts[1]});
    await timeMachine.advanceBlockAndSetTime(timeRound1+100);
    amount += 10000;
    await assertRevert(AuctionInstance.openCommitment(orderHash, amount, price, nonce, {from: accounts[1], value: fee}));
    
    // Too many shares: 10005 shares to open
    orderHash = getHash(amount,price,accounts[1],nonce);

    await timeMachine.advanceBlockAndSetTime(timeRound1-100);
    await AuctionInstance.submitCommitment(orderHash, {from: accounts[1]});
    await timeMachine.advanceBlockAndSetTime(timeRound1+100);
    await assertRevert(AuctionInstance.openCommitment(orderHash, amount, price, nonce, {from: accounts[1], value: fee}));
  
    // Too low price
    price = 1;
    orderHash = getHash(amount,price,accounts[1],nonce);
    await timeMachine.advanceBlockAndSetTime(timeRound1-100);
    await AuctionInstance.submitCommitment(orderHash, {from: accounts[1]});
    await timeMachine.advanceBlockAndSetTime(timeRound1+100);
    await assertRevert(AuctionInstance.openCommitment(orderHash, amount, price, nonce, {from: accounts[1], value: fee}));
    
    // Not paying
    price = basePrice;
    amount = 5;
    fee = price*amount;
    nonce = 4;
    orderHash = getHash(amount,price,accounts[1],nonce);
    await timeMachine.advanceBlockAndSetTime(timeRound1-100);
    await AuctionInstance.submitCommitment(orderHash, {from: accounts[1]});
    await timeMachine.advanceBlockAndSetTime(timeRound1+100);
    await assertRevert(AuctionInstance.openCommitment(orderHash, amount, price, nonce, {from: accounts[1], value: 0}));
  });
  it('Round 2 sorted', async () => {
    priceWei = [0,0,0,0,0,0];
    price = [baseEther, baseEther+1, baseEther+4, baseEther+4,baseEther+3, baseEther+10];
    amount = [web3.utils.toBN(5),web3.utils.toBN(5),web3.utils.toBN(5),web3.utils.toBN(5),web3.utils.toBN(5),web3.utils.toBN(5)];
    fee = [0,0,0,0,0,0];
    orderHash = [0,0,0,0,0,0];
    nonce = 1;

    // Submit orders first
    await timeMachine.advanceBlockAndSetTime(timeRound1-1000000);
    for (i = 0; i < 6; i++)
    {
      priceWei[i] = web3.utils.toWei(web3.utils.toBN(price[i]),'ether');
      orderHash[i] = getHash(amount[i], priceWei[i], accounts[i], nonce);
      await AuctionInstance.submitCommitment(orderHash[i], {from: accounts[i]});
      fee[i] = price[i] * amount[i];
      fee[i] = web3.utils.toWei(web3.utils.toBN(fee[i]),'ether');
    }

    // Time to round 2
    await timeMachine.advanceBlockAndSetTime(timeRound1+100);
    for (i = 0; i < 6; i++)
    {
      await AuctionInstance.openCommitment(orderHash[i], amount[i], priceWei[i], nonce, {from: accounts[i], value: fee[i]});
    }
    
    correctOrder = [5,2,3,4,1,0]
    for (i = 0; i < 6; i++)
    {
      orders = await AuctionInstance.openOrders(i);
      assert(orders.bidder == accounts[correctOrder[i]]);
    }
  });
  
  it('Faulty Issue', async () => {
    // Too early
    await timeMachine.advanceBlockAndSetTime(timeRound1-1000000);
    await assertRevert(AuctionInstance.issue());

    // No orders opened
    await timeMachine.advanceBlockAndSetTime(timeRound2+100);
    await assertRevert(AuctionInstance.issue({from: accounts[0]}));

    // Go back to round 1
    await timeMachine.advanceBlockAndSetTime(timeRound1-1000000);
    priceWei = 0;
    price = baseEther;
    amount = 5;
    nonce = 1;
    fee = price * amount;
    fee = web3.utils.toWei(web3.utils.toBN(fee),'ether');
    priceWei = web3.utils.toWei(web3.utils.toBN(price),'ether');
    orderHash = getHash(amount, priceWei, accounts[0], nonce);
    await AuctionInstance.submitCommitment(orderHash, {from: accounts[0]});

    // Time to round 2
    await timeMachine.advanceBlockAndSetTime(timeRound1+100);
    await AuctionInstance.openCommitment(orderHash, amount, priceWei, nonce, {from: accounts[0], value: fee});
    
    // After round 2
    await timeMachine.advanceBlockAndSetTime(timeRound2+100);
    await AuctionInstance.issue({from: accounts[0]});
    await assertRevert(AuctionInstance.issue({from: accounts[0]}));
  });

  it('Issue and ERC20 shares functioning', async () => {
    priceWei = [0,0,0];
    price = [baseEther+2, baseEther+1, baseEther];
    amount = [web3.utils.toBN(5),web3.utils.toBN(10000),web3.utils.toBN(5)];
    fee = [0,0,0];
    orderHash = [0,0,0];
    nonce = 1;

    // Submit orders first
    await timeMachine.advanceBlockAndSetTime(timeRound1-1000000);
    for (i = 0; i < 3; i++)
    {
      priceWei[i] = web3.utils.toWei(web3.utils.toBN(price[i]),'ether');
      orderHash[i] = getHash(amount[i], priceWei[i], accounts[i], nonce);
      await AuctionInstance.submitCommitment(orderHash[i], {from: accounts[i]});
      fee[i] = price[i] * amount[i];
      fee[i] = web3.utils.toWei(web3.utils.toBN(fee[i]),'ether');
    }

    // Time to round 2
    await timeMachine.advanceBlockAndSetTime(timeRound1+100);
    for (i = 0; i < 3; i++)
    {
      await AuctionInstance.openCommitment(orderHash[i], amount[i], priceWei[i], nonce, {from: accounts[i], value: fee[i]});
    }
    
    // Issue
    await timeMachine.advanceBlockAndSetTime(timeRound2+100);

    // Check balance is correct
    correctBalance = ["5", "9995", "0"];
    for (i = 0; i < 3; i++)
    {
      await AuctionInstance.issue({from: accounts[i]});
      let balance = await Shares.balanceOf(accounts[i]);
      assert.equal(balance.toString(10), correctBalance[i], "Incorrect Balance");
    }

    // Transfer from account 1 to 0
    await Shares.transfer(accounts[0], 5, {from: accounts[1]});
    balance = await Shares.balanceOf(accounts[0]);
    assert.equal(balance.toString(10), 10, "Incorrect Balance");
    balance = await Shares.balanceOf(accounts[1]);
    assert.equal(balance.toString(10), 9990, "Incorrect Balance");

    // Approve
    // 1 Allow account 2 to transfer, and accounts transfer from 1 to 2.
    await Shares.approve(accounts[2], 10, {from: accounts[1]});
    balance = await Shares.allowance(accounts[1], accounts[2]);
    assert.equal(balance.toString(10), 10, "Incorrect Balance");
    await Shares.transferFrom(accounts[1], accounts[2], 10, {from: accounts[2]});
    balance = await Shares.balanceOf(accounts[2]);
    assert.equal(balance.toString(10), 10, "Incorrect Balance");

  });
});
