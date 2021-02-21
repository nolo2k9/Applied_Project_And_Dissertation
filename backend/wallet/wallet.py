import uuid
import json
from backend.config import STARTING_BALANCE

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec # Eliptic cryptography module
from cryptography.hazmat.primitives import hashes, serialization # Import hashing and serialization implementations
from cryptography.hazmat.primitives.asymmetric.utils import (
    encode_dss_signature, # digital signature standard
    decode_dss_signature
)
from cryptography.exceptions import InvalidSignature


class Wallet:
    """
    An individual miners wallet.
    Wallets keep track of a miners balance.
    Allows a miner to authorize transactions.
    """

    def __init__(self, blockchain = None):
        self.blockchain = blockchain
        """
        Wallet address first 8 characters from a uuid 
        https://docs.python.org/3/library/uuid.html

        """
        self.address = str(uuid.uuid4())[0:8]
       
        """
        Setting the wallets private key to the result of calling this function.
        SECP256K1(): Eliptic base algorithm: Standards of effiecient cryptography Prime 256 bits
        A prime number is used to generate the curve which will be represented in 256 bits
        """
        # Public and private key pair
        self.private_key = ec.generate_private_key(
            ec.SECP256K1(), default_backend())
        # Assigning public_key according to self.private_key.public_key()
        self.public_key = self.private_key.public_key()
        self.serialize_public_key()
    
    """
    @Property allows the code in this method to be ran each time the wallet.balance attribute is used.
    """
    @property
    def balance(self):
        
        return Wallet.calculate_balance(self.blockchain, self.address)
        
        
        
        

    def sign(self, data):
        """
        This method generates a signature based on the data using the local private key.

        Takes the data that needs to be signed and the ECDSA method from the elipical curve algorithm.
        ECDSA- Eliptical Curve Cryptography Digital Signature Algorithm.
        Takes in a hashing implementation SHA 256
        Json dumps stringifys the data
        """
        return decode_dss_signature(self.private_key.sign(
            json.dumps(data).encode('utf-8'),
            ec.ECDSA(hashes.SHA256())
        ))

    def serialize_public_key(self):
        """
        Resets public key to its serialized version
        """
        # reassign public_key to decoded version
        self.public_key = self.public_key.public_bytes(
            encoding = serialization.Encoding.PEM, 
            format = serialization.PublicFormat.SubjectPublicKeyInfo # represent public key as a byte string
        ).decode('utf-8') # back to a regular string 

    @staticmethod
    def verify(public_key, data, signature):
        """
        This method verify's a signature based on the wallets public and data.
        """
        # incoming key is a string, we need to turn it back into something readable by the method
        deserialized_public_key = serialization.load_pem_public_key(
            public_key.encode('utf-8'),
            default_backend()
        )

        (r, s) = signature

        try:
            deserialized_public_key.verify(
                encode_dss_signature(r, s), 
                json.dumps(data).encode('utf-8'), 
                ec.ECDSA(hashes.SHA256()))
            return True
        # catch Invalid Signature exception
        except InvalidSignature:
            return False

    @staticmethod
    def calculate_balance(blockchain, address):
        """
        Calculate the balance of the given address considering the transaction data within the blockchain.
        The balance is found by adding the output the values that belong to the address 
        since the most recent transaction by that address.
        """
        balance = STARTING_BALANCE
        
        if not blockchain:
            return balance
            

        for block in blockchain.chain:
            for transaction in block.data:
                if transaction['input']['address'] == address:
                    # Any time the address does a new transaction it resets its balance
                    balance = transaction['output'][address]
                elif address in transaction['output']:
                    balance += transaction['output'][address]
        
        return balance

def main():
    wallet = Wallet()
    print(f'wallet.__dict__: {wallet.__dict__}') # print wallet dictionary
    # Generate a signature
    data = {'foo': 'bar'}
    signature = wallet.sign(data)
    print(f'signature: {signature}')
    # Testing a valid wallet verification
    should_be_valid = Wallet.verify(wallet.public_key, data, signature)
    print(f'should be valid: {should_be_valid}')

    # Testing an invalid wallet verification (random wallet)
    should_be_invalid = Wallet.verify(Wallet().public_key, data, signature)
    print(f'should not be valid: {should_be_invalid}')


if __name__ == '__main__':
    main()
