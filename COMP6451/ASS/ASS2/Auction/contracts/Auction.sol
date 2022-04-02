// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;
import "./NeverPayShares.sol";

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
        address bidder;
        uint number;    // short name (up to 32 bytes)
        uint price;     // number of accumulated votes
        uint indicator;
    }

    Order[] public openOrders;

    mapping(bytes32 => uint) orders; //TODO remove public
    mapping(bytes32 => bool) opened;
    mapping(address => bool) issued;
    address issuer;
    uint numOrders = 0;
    IERC20 public shares;
    constructor()
    {
        issuer = msg.sender;
        shares = new NeverPayShares(numberShares);
    }

    function hash(uint number, uint price, address addr, uint nonce) 
    public pure
    returns (bytes32) 
    {
        return keccak256(abi.encode(number, price, nonce, addr));
    }

    function submitCommitment(bytes32 newOrder) public {
        require(
            block.timestamp < 1650412800,//Timestamp for 20-04-2022-00:00:00-GMT
            "The first round has ended."
        );
        if (orders[newOrder] != 0)
            return;
        numOrders++;
        orders[newOrder] = numOrders;
    }

    function openCommitment(bytes32 orderHash, uint number, uint price, uint nonce) payable public {
        require(
            block.timestamp >= 1650412800,//Timestamp for 20-04-2022-00:00:00-GMT
            "The second round hasn't started."
        );
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
        openOrders.push(Order(msg.sender, number, price, 10000000000*price+orders[orderHash]));
        opened[orderHash] = true;
        quickSort(openOrders, 0, int(openOrders.length)-1);
    }

    function issue() public
    {
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
        issued[msg.sender] = true;
    }

    function refund(Order storage refundOrder, uint unitIssued) private
    {
        uint amount = (refundOrder.number - unitIssued) * refundOrder.price;
        address payable payee = payable(refundOrder.bidder);
        (bool success, ) = payee.call{value: amount}("");
        require(success, "Failed to send Ether");
    }

    function settle(Order storage refundOrder, uint unitIssued) private
    {
        uint amount = unitIssued * refundOrder.price;
        address payable payee = payable(issuer);
        (bool success, ) = payee.call{value: amount}("");
        require(success, "Failed to send Ether to issuer");
    }

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
}
