const Web3EthAccounts = require('web3-eth-accounts');
const abi = require('web3-eth-abi');
const utils = require('web3-utils');

function getSignHash(addr, message, year)
{
  const encoded = abi.encodeParameters(['address','string', 'uint256'],[addr, message, year]);
  const orderHash = utils.soliditySha3(encoded);
  return orderHash;
}

const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

const account = new Web3EthAccounts('ws://localhost:8546');
Acc = account.create();
// console.log(Acc);

readline.question('What is the investor\'s address?\n', addr => {
    message = 'The owner of Ethereum address '+addr+' is a sophisticated investor for year 2022.'
    console.log("Message:\n"+ message);
    hashi = getSignHash(addr, message, 2022);
    console.log("Message hash:\n"+ hashi);
    console.log("Public Key:\n"+ Acc['address']);
    data = account.sign(hashi, Acc.privateKey);
    console.log("Signature:\n"+ data['signature']);
    readline.close();
});

// The owner of Ethereum address 0x5B38Da6a701c568545dCfcB03FcB875f56beddC4 is a sophisticated investor for year 2022