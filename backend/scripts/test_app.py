import requests
import time

from backend.wallet.wallet import Wallet

"""
This script is for testing endpoint probes.
Testing transactions GET and POST results as one return in the command line.
"""

BASE_URL = 'http://localhost:5000'

def get_blockchain():
    return requests.get(f'{BASE_URL}/blockchain').json()

def get_blockchain_mine():
    return requests.get(f'{BASE_URL}/blockchain/mine').json()

def post_wallet_transact(recipient, amount):
    return requests.post(f'{BASE_URL}/wallet/transact',
    json = {'recipient': recipient, 'amount': amount}
).json() # as json


"""
initializing and printing test output
"""
start_blockchain = get_blockchain()
print(f'start_blockchain: {start_blockchain}')

recipient = Wallet().address

post_wallet_transact_1 = post_wallet_transact(recipient, 21)
print(f'\npost_wallet_transact_1:{post_wallet_transact_1}')

time.sleep(1) # allows requests to come in so as to not choke up the queue
post_wallet_transact_2 = post_wallet_transact(recipient, 13)
print(f'\npost_wallet_transact_2:{post_wallet_transact_2}')

time.sleep(1)
mined_block = get_blockchain_mine()
print(f'\nmined_block: {mined_block}')