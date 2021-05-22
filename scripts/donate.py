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

from web3 import Web3, HTTPProvider, IPCProvider
from web3.middleware import geth_poa_middleware
import requests

url = "https://rpc.cheapeth.org/rpc"
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
print(web3.fromWei(balance, "ether"))

# setting donation contract
abi_url = "https://raw.githubusercontent.com/CheapEthereum/GoFundGeohot/master/data/abi/GoFundGeohot.json"
abi = requests.get(abi_url).text
donate_contract = web3.eth.contract(
    abi=abi,
    address=web3.toChecksumAddress("0x891F4cdA9738E0E77D5a12cd209EdB9cbFae30c7"),
)
print("Beneficiary address: {}".format(donate_contract.functions.getBeneficiary().call()))

amount_to_revert = 1
revert_amount = Web3.toWei(amount_to_revert, "ether")

# preparing tx
donate_transaction = donate_contract.functions.unDonate(
    amount=revert_amount
).buildTransaction(
    {
        "from": self_address,
        "gasPrice": Web3.toWei(1, "gwei"),
        "gas": 90000,
        "nonce": web3.eth.getTransactionCount(self_address)
    }
)
signed_donate_transaction = web3.eth.account.signTransaction(
    donate_transaction, private_key_hex
)
raw_tx_hex = Web3.toHex(signed_donate_transaction.rawTransaction)

# sending tx
tx_hash = web3.eth.sendRawTransaction(raw_tx_hex)
print(tx_hash.hex())
signed_donate_transaction = web3.eth.account.signTransaction(donate_transaction, private_key_hex)
raw_tx_hex = Web3.toHex(signed_donate_transaction.rawTransaction)

# sending tx
tx_hash = web3.eth.sendRawTransaction(raw_tx_hex)
print(tx_hash.hex())


"""
The above code works!

Note: it turns out we need to pass "amount" as a function parameter
and *not* as key-value pair to the data dictionary for buildTransaction.
"""