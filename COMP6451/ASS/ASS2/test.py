import web3

encoded = web3.eth.abi.encodeParameters(['uint256', 'uint256', 'uint256', 'address'], [5,5,1,'0x5B38Da6a701c568545dCfcB03FcB875f56beddC4']);
data = web3.tuils.soliditySha3(encoded)
print(data)
