#Import flask
from flask import Flask, jsonify
#Import the Blockchain class
from backend.blockchain.blockchain import Blockchain
#Import pubsub class
from backend.pubsub import PubSub

import os
import random


app = Flask(__name__)
blockchain = Blockchain()
pubsub = PubSub()

@app.route('/')
def route_default():
    return 'Welcome to the Delta coin blockchain'

@app.route('/blockchain')
def route_blockchain():
    #Wrapping call to blockchain with jsonify
    return jsonify(blockchain.to_json())

@app.route('/blockchain/mine')
def route_blockchain_mine():
    #Temp transaction data
    transaction_data = 'stubbed_transaction_data'
    #Data for new block with temp data
    blockchain.add_block(transaction_data)
    #Display new block mined
    return jsonify(blockchain.chain[-1].to_json())

# define our port and conditions
PORT = 5000
# Choose random port in the range
if os.environ.get('PEER') == 'True':
    PORT = random.randint(5001, 6000)

# run app on our port
app.run(port=PORT)