# Import flask
from flask import Flask, jsonify, request
# Import the Blockchain class
from backend.blockchain.blockchain import Blockchain
# Import pubsub class
from backend.pubsub import PubSub

from backend.wallet.wallet import Wallet
from backend.wallet.transaction import Transaction

import os
import random
import requests


app = Flask(__name__)
blockchain = Blockchain()
pubsub = PubSub(blockchain)
wallet = Wallet()


@app.route('/')
def route_default():
    return 'Welcome to the Delta coin blockchain'


@app.route('/blockchain')
def route_blockchain():
    # Wrapping call to blockchain with jsonify
    return jsonify(blockchain.to_json())


@app.route('/blockchain/mine')
def route_blockchain_mine():
    # Temp transaction data
    transaction_data = 'stubbed_transaction_data'
    # Data for new block with temp data
    blockchain.add_block(transaction_data)
    # Display new block mined
    block = blockchain.chain[-1]
    pubsub.broadcast_block(block)
    return jsonify(block.to_json())

# Generate a new transaction instance
@app.route('/wallet/transact', methods=['POST'])
def route_wallet_transact():
    # pass in wallet for the transaction
    transaction_data = request.get_json() # as json
    # creates a valid transaction instance
    transaction = Transaction(
        wallet,
        transaction_data['recipient'],
        transaction_data['amount']
    )

    print(f'transaction.to_json():  {transaction.to_json()}')

    return jsonify(transaction.to_json())

# define our port and conditions
ROOT_PORT = 5000
PORT = ROOT_PORT
# Choose random port in the range
if os.environ.get('PEER') == 'True':
    PORT = random.randint(5001, 6000)

    result = requests.get(f'http://localhost:{ROOT_PORT}/blockchain')
    result_blockchain = Blockchain.from_json(result.json())

    try:
        blockchain.replace_chain(result_blockchain.chain)
        print('\n -- Successfully synchronized the local chain')
    except Exception as e:
        print(f'\n -- Error synchronizing: {e}')

# run app on our port
app.run(port=PORT)
