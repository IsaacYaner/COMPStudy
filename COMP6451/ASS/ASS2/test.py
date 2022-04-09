import web3

data = web3.personal.sign(hash, web3.eth.defaultAccount)
print(data)
