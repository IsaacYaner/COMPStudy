// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

/** 
 * @title Bidding
 * @dev Implements bidding function for NerverPay
 */

contract SophisticatedInvestorCertificateAuthorityRegistry
{
    mapping(address => bool) authorised;
    address ASIC;

    constructor()
    {
        ASIC = msg.sender;
    }

    /*
    Add pubKey to authorised list.
    */
    function authorise(address pubKey) public
    {
        require(msg.sender == ASIC);
        authorised[pubKey] = true;
    }
    /*
    Add pubKey from authorised list.
    */
    function cancel(address pubKey) public
    {
        require(msg.sender == ASIC);
        authorised[pubKey] = false;
    }
    /*
    Return whether pubKey is authorised.
    */
    function isAuthorised(address pubKey) public view returns (bool)
    {
        return authorised[pubKey];
    }

    /*
    Called by verify(), return the hash of the message.
    */
    function getMessageHash(
        address _investor,
        string memory _message,
        uint256 year
    ) public pure returns (bytes32) {
        return keccak256(abi.encode(_investor, _message, year));
    }

    /*
    Called by verify(), return the signature of messageHash
    */
    function getEthSignedMessageHash(bytes32 _messageHash)
        public
        pure
        returns (bytes32)
    {
        // Signature is generated in the following format:
        // "\x19Ethereum Signed Message\n" + len(msg) + msg
        return
            keccak256(
                abi.encodePacked("\x19Ethereum Signed Message:\n32", _messageHash)
            );
    }

    /*
    Parameters:
        address signer:     public key
        address investor:   investor address used in message encryption
        uint256 year:       The year that sign the message
        bytes signature:    the signature that is going to be verified
    Effect:
        Induce the signer using the information given, and then compare with 
            the signer passed in.
    Return:
        return the validity
    */
    function verify(
        address _signer,
        address _investor,
        uint256 year,
        string memory _message,
        bytes memory signature
    ) public view returns (bool) 
    {
        if (authorised[_signer] == false)
        {
            return false;
        }
        bytes32 messageHash = getMessageHash(_investor, _message, year);
        bytes32 ethSignedMessageHash = getEthSignedMessageHash(messageHash);
        return recoverSigner(ethSignedMessageHash, signature) == _signer;
    }

    // Use ecrecover to recover signer
    // Return: address: publicKey(signer)
    function recoverSigner(bytes32 _ethSignedMessageHash, bytes memory _signature)
        public
        pure
        returns (address)
    {
        (bytes32 r, bytes32 s, uint8 v) = splitSignature(_signature);

        return ecrecover(_ethSignedMessageHash, v, r, s);
    }

    function splitSignature(bytes memory sig)
        public
        pure
        returns (bytes32 r, bytes32 s, uint8 v )
    {
        require(sig.length == 65, "invalid signature length");

        assembly {
            r := mload(add(sig, 32))
            s := mload(add(sig, 64))
            v := byte(0, mload(add(sig, 96)))
        }

    }
}


