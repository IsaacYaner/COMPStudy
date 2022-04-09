// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;
import "./NeverPayShares.sol";
import "./Certificates.sol";

/** 
 * @title Bidding
 * @dev Implements bidding function for NerverPay
 */

contract Auction
{
    uint numberShares = 10000;              // Maximum number of shares
    uint minPrice = 1000000000000000000;    // Valued by Wei, i.e. 1ETH
    uint orderNum = 0;                      // Number of orders

    struct Order 
    {
        address bidder; // Address of bidder
        uint number;    // short name (up to 32 bytes)
        uint price;     // number of accumulated votes
        uint indicator; // Used for sorting
    }

    Order[] public openOrders;

    mapping(bytes32 => uint) orders;    // #id of the order hash
    mapping(bytes32 => bool) opened;    // whether the order with the hash is opened
    mapping(address => bool) issued;    // whether the investor with the address has called issue() 
    mapping(bytes32 => address) owner;  // Address of the one who submit the order
    mapping(address => bool) verified;  // Whether the investor has verified
    address issuer;         // The one who receive ethereum ultimately
    uint numOrders = 0;     // Number of orders submitted, used for counting #id 
    IERC20 public shares;   // Address of shares contract
    SophisticatedInvestorCertificateAuthorityRegistry public registry;  // Address of sophiscated inv. registry
    constructor(address registryAddr)
    {
        issuer = msg.sender;    // Record the owner as issuer.
        shares = new NeverPayShares(numberShares);  // Construct new shares contract
        registry = SophisticatedInvestorCertificateAuthorityRegistry(registryAddr); //Pass the address in 
    }

    /*
    Parameters:
        uint number:  numbers of shares to buy
        uint price:   price per share, unit in Wei
        address addr: investor address
        uint nonce:   Identifier for orders with the same (number, price, address)
    Return:
        byte32 hash of the order information.
    */
    function hash(uint number, uint price, address addr, uint nonce) 
    public pure
    returns (bytes32) 
    {
        return keccak256(abi.encode(number, price, nonce, addr));
    }
    /*
    Parameters:
        byte32 newOrder: hash of the order to be submitted
    Effect:
        Add the order to orders list, and record the message
            sender as the owner of this order.
    */
    function submitCommitment(bytes32 newOrder) public {
        // COMMENT THIS
        require(
            block.timestamp < 1650412800,//Timestamp for 20-04-2022-00:00:00-GMT
            "The first round has ended."
        );
        require(
            verified[msg.sender] == true,
            "You haven't been verified as a sophiscated investor."
        );
        if (orders[newOrder] != 0)
            return;
        numOrders++;
        orders[newOrder] = numOrders;
        owner[newOrder] = msg.sender;
    }

    /*
    Parameters:
        byte32 newOrder: hash of the order to be submitted
    Effect:
        Remove newOrder from orders list.
    */
    function withdraw(bytes32 newOrder) public {
        // COMMENT THIS
        require(
            block.timestamp < 1650412800,//Timestamp for 20-04-2022-00:00:00-GMT
            "The first round has ended."
        );
        require(
            msg.sender == owner[newOrder],//Timestamp for 20-04-2022-00:00:00-GMT
            "Only the owner can withdraw the order."
        );
        if (orders[newOrder] == 0)
            return;
        orders[newOrder] = 0;
    }

    /*
    Parameters:
        byte32 orderHash:   hash of the order to be submitted
        uint number:        numbers of shares to buy
        uint price:         price per share, unit in Wei
        address addr:       investor address
        uint nonce:         Identifier for orders with the same (number, price, address)
    Effect:
        Construct an order instance, add the order to openOrders list, and the sort the list.
    */
    function openCommitment(bytes32 orderHash, uint number, uint price, uint nonce) payable public {
        // COMMENT THIS
        require(
            block.timestamp >= 1650412800,//Timestamp for 20-04-2022-00:00:00-GMT
            "The second round hasn't started."
        );
        // COMMENT THIS
        require(
            block.timestamp < 1651017600,//Timestamp for 27-04-2022-00:00:00-GMT
            "The second round has ended."
        );
        require(
            orders[orderHash] != 0,
            "Order doesn't exist."
        );
        require(
            hash(number, price, msg.sender, nonce) == orderHash,
            "Wrong orderHash."
        );
        require(
            number <= 10000,
            "There are at most 10000 shares issued."
        );
        require(
            price >= minPrice,
            "The minimum price per share is 1 Ether."
        );
        require(
            price*number == msg.value,
            "Please pay appropriate amount of Eth."
        );
        require(                
            opened[orderHash] == false,
            "This order has been opened."
        );
        // Max uint is about 10^77, and the base price is 1^18 Wei, so
        // Multiplying price by 1^10 is not likely to cause overflow.
        openOrders.push(Order(msg.sender, number, price, 10000000000*price-orders[orderHash]));
        opened[orderHash] = true;
        quickSort(openOrders, 0, int(openOrders.length)-1);
    }

    /*
    Parameters:
        msg.sender (implied)
    Effect:
        Issue the first 10,000 shares, settle the deposited ethereums to the issuer, and
            transfer the shares to bidder. Then refund any unissued orders back to the
            investors.
        Then set msg.sender to issued. 
    */
    function issue() public
    {
        // COMMENT THIS
        require(
            block.timestamp >= 1651017600,//Timestamp for 27-04-2022-00:00:00-GMT
            "The second round hasn't end."
        );
        require(
            openOrders.length > 0,
            "No order is opened."
        );
        require(
            issued[msg.sender] == false,
            "Already issued."
        );
        uint remainingShares = numberShares;
        issued[msg.sender] = true;
        for (uint i = 0; i < openOrders.length; i++)
        {
            if (openOrders[i].number <= remainingShares)
            {
                // Issue full order.
                if (openOrders[i].bidder == msg.sender)
                {
                    settle(openOrders[i], openOrders[i].number);
                    shares.transfer(openOrders[i].bidder, openOrders[i].number);
                }
                remainingShares -= openOrders[i].number;
            }
            else
            {
                // Refund (number - remainingShares) * price
                if (openOrders[i].bidder == msg.sender)
                {
                    refund(openOrders[i], remainingShares);
                }
                if (remainingShares != 0)
                {
                    // Issue remainingShares.
                    if (openOrders[i].bidder == msg.sender)
                    {
                        settle(openOrders[i], remainingShares);
                        shares.transfer(openOrders[i].bidder, remainingShares);
                    }
                    remainingShares = 0;
                }
            }
        }
    }

    // Called by issue() only, refund refundOrder.number - unitIssued to bidder of the order
    function refund(Order storage refundOrder, uint unitIssued) private
    {
        uint amount = (refundOrder.number - unitIssued) * refundOrder.price;
        address payable payee = payable(refundOrder.bidder);
        (bool success, ) = payee.call{value: amount}("");
        require(success, "Failed to send Ether");
    }

    // Called by issue() only, transfer issued eths to issuer
    function settle(Order storage refundOrder, uint unitIssued) private
    {
        uint amount = unitIssued * refundOrder.price;
        address payable payee = payable(issuer);
        (bool success, ) = payee.call{value: amount}("");
        require(success, "Failed to send Ether to issuer");
    }

    // sort the order list in descending order according to indicator.
    function quickSort(Order[] storage arr, int left, int right) private
    {
        int i = left;
        int j = right;
        if (i == j) return;
        uint pivot = arr[uint(left + (right - left) / 2)].indicator;
        while (i <= j) {
            while (arr[uint(i)].indicator > pivot) i++;
            while (pivot > arr[uint(j)].indicator) j--;
            if (i <= j) {
                Order memory temp = arr[uint(j)];
                arr[uint(j)] = arr[uint(i)];
                arr[uint(i)] = temp;
                i++;
                j--;
            }
        }
        if (left < j)
            quickSort(arr, left, j);
        if (i < right)
            quickSort(arr, i, right);
    }

    /*
    Parameters:
        address _signer:    public key of the signature
        string message:     the signed message
        bytes signature:    signature of the message
    Effect:
        Call verify() of registry, set verified[msg.sender] to true if it is valid.
        Then return the verification result.  
    */
    function verify(
        address _signer,
        string memory _message,
        bytes memory signature
    ) public returns (bool) 
    {
        if (registry.verify(_signer, msg.sender, 2022, _message, signature) == true)
        {
            verified[msg.sender] = true;
            return true;
        }
        return false;
    }
}
