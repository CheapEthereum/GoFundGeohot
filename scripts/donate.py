from web3 import Web3, HTTPProvider, IPCProvider
from web3.middleware import geth_poa_middleware
import requests

url = 'https://rpc.cheapeth.org/rpc'
web3 = Web3(HTTPProvider(url))

# inject the poa compatibility middleware to the innermost layer
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

# use your own private key
private_key_hex = "XXX"

# setting account checking balance
my_account = web3.eth.account.from_key(private_key_hex)
self_address = my_account.address
print("__________________balance___________________")
balance = web3.eth.getBalance(my_account.address)
print(web3.fromWei(balance, 'ether'))

# setting donation contract
abi_url = 'https://raw.githubusercontent.com/CheapEthereum/GoFundGeohot/master/data/abi/GoFundGeohot.json'
abi = requests.get(abi_url).text
donate_contract = web3.eth.contract(abi=abi, address=web3.toChecksumAddress('0x891F4cdA9738E0E77D5a12cd209EdB9cbFae30c7'))
print('Beneficiary address: {}'.format(donate_contract.functions.getBeneficiary().call()))

amount_to_get_back = Web3.toWei(0.1, 'ether')  # do we need the amount of one of the transactions we want to get back?

# preparing tx
donate_transaction = donate_contract.functions.unDonate()\
.buildTransaction({
    'from': self_address,
    'gasPrice':  Web3.toWei(0.1, 'gwei'),
    'gas': 90000,
    'amount': amount_to_get_back,
    'nonce': web3.eth.getTransactionCount(self_address),
})
signed_donate_transaction = web3.eth.account.signTransaction(donate_transaction, private_key_hex)
raw_tx_hex = Web3.toHex(signed_donate_transaction.rawTransaction)

# sending tx
tx_hash = web3.eth.sendRawTransaction(raw_tx_hex)
print(tx_hash.hex())


"""
Now we get:

web3.exceptions.ValidationError: 
Could not identify the intended function with name `unDonate`, positional argument(s) of type `()` and keyword argument(s) of type `{}`.
Found 1 function(s) with the name `unDonate`: ['unDonate(uint256)']
Function invocation failed due to improper number of arguments.

"""