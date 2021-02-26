# Import flask
from flask import Flask, jsonify, request
# Import the Blockchain class
from backend.blockchain.blockchain import Blockchain
# Import pubsub class
from backend.pubsub import PubSub

from backend.wallet.wallet import Wallet
from backend.wallet.transaction import Transaction
from backend.wallet.transaction_pool import TransactionPool
#Import flask middleware
from flask_cors import CORS

import os
import random
import requests


app = Flask(__name__)
#Enable Cors
CORS(app, resourses={r'/*':{'origins': 'http://localhost:3000'} })
blockchain = Blockchain()
wallet = Wallet(blockchain)
transaction_pool = TransactionPool()
pubsub = PubSub(blockchain, transaction_pool)


@app.route('/')
def route_default():
    return 'Welcome to the Delta coin blockchain'


@app.route('/blockchain')
def route_blockchain():
    # Wrapping call to blockchain with jsonify
    return jsonify(blockchain.to_json())

@app.route('/blockchain/range')
def route_blockchain_range():
    #Start and end points casted to an int
    start = int(request.args.get('start'))
    end = int(request.args.get('end'))
    #Return a slice of the data between the two points. Return the list starting from the most recent block
    return jsonify(blockchain.to_json()[::-1][start:end])

#Return the length of the blockchain
@app.route('/blockchain/length')
def route_blockchain_length():
    return jsonify(len(blockchain.chain))

@app.route('/blockchain/mine')
def route_blockchain_mine():
    transaction_data = transaction_pool.transaction_data()
    #Reward the local wallet (Your wallet)
    transaction_data.append(Transaction.reward_transaction(wallet).to_json())
    # Data for new block with temp data
    blockchain.add_block(transaction_data)
    # Display new block mined
    block = blockchain.chain[-1]
    pubsub.broadcast_block(block)
    transaction_pool.clear_blockchain_transactions(blockchain)

    return jsonify(block.to_json())

# Generate a new transaction instance
@app.route('/wallet/transact', methods=['POST'])
def route_wallet_transact():
    # pass in wallet for the transaction
    transaction_data = request.get_json() # as json
    # creates a valid transaction instance
    transaction = transaction_pool.existing_transaction(wallet.address)

    # Check for existing then update, otherwise make a new transaction
    if transaction:
        transaction.update(
            wallet,
            transaction_data['recipient'],
            transaction_data['amount']
        )
    else:
        transaction = Transaction(
            wallet,
            transaction_data['recipient'],
            transaction_data['amount']
        )

    pubsub.broadcast_transaction(transaction)

    return jsonify(transaction.to_json())
#Access your wallets information from the api
@app.route('/wallet/info')
def route_wallet():
    #Returns the address and balance of the wallet.
    return jsonify({'address': wallet.address,'balance': wallet.balance })
    
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
        
#Automatically create 10 blocks with 2 transactions each in the backend
if os.environ.get('SEED_DATA') == 'True':
    for i in range(10):
        blockchain.add_block([
            #Instantiating wallet, random address and random amount
            Transaction(Wallet(), Wallet().address, random.randint(2,50)).to_json(),
            Transaction(Wallet(), Wallet().address, random.randint(2,50)).to_json()
        ])
        

# run app on our port
app.run(port=PORT)
