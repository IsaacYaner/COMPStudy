from eth_abi import encode_single, encode_abi
from web3 import Web3, EthereumTesterProvider
from Crypto.Hash import keccak
import pyperclip

import binascii
number = int(input("Number:"))
price = int(input("Price:"))
nonce = int(input("identifier/nonce:"))
address = input("Address:")

k = keccak.new(digest_bits=256)
data = encode_abi(['uint256', 'uint256', 'uint256', 'address'], [number, price, nonce, address])
k.update(data)
data = '0x' + k.hexdigest()
print("Order hash is: ", data)
pyperclip.copy(data)
print("Hash copied to paperclip.")