#Import flask
from flask import Flask
#Import the Blockchain class
from backend.blockchain.blockchain import Blockchain

app = Flask(__name__)
blockchain = Blockchain()

@app.route('/')
def route_default():
    return 'Welcome to the Delta coin blockchain'

#Test data add more blocks
for i in range(3):
    blockchain.add_block(i)

@app.route('/blockchain')
def route_blockchain():
    #Return the __repr__ this makes the data readable by flask
    return blockchain.__repr__()


app.run()