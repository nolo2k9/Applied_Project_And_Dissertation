import uuid
import json
from backend.config import STARTING_BALANCE

from cryptography.hazmat.backends import default_backend

#Eliptic cryptography module 
from cryptography.hazmat.primitives.asymmetric import ec
# Import hashing implmentation
from cryptography.hazmat.primitives import hashes


class Wallet:
    """
    An individual miners wallet.
    Wallets keep track of a miners balance.
    Allows a miner to authorize transactions.
    """
    
            
    def __init__(self):
        """
        Wallet address first 8 characters from a uuid 
        https://docs.python.org/3/library/uuid.html
        
        """
        self.address = str(uuid.uuid4())[0:8]
        #Wallet balance
        self.balance = STARTING_BALANCE
        """
        Setting the wallets private key to the result of calling this function.
        SECP256K1(): Eliptic base algorithm: Standards of effiecient cryptography Prime 256 bits
        A prime number is used to generate the curve which will be represented in 256 bits
        """
        #Public and private key pair
        self.private_key = ec.generate_private_key(ec.SECP256K1(), default_backend())
        #Assigning public_key according to self.private_key.public_key()
        self.public_key = self.private_key.public_key()
        
    def sign(self, data):
        """
        This method generates a signature based on the data using the local private key.
        """
        """
        Takes the data that needs to be signed and the ECDSA method from the elipical curve algorithm.
        ECDSA- Eliptical Curve Cryptography Digital Signature Algorithm.
        Takes in a hashing implementation SHA 256
        Json dumps stringifys the data
        """
        return self.private_key.sign(json.dumps(data).encode('utf-8'), 
                                     ec.ECDSA(hashes.SHA256())
                                     )
       
        
    
        
            
        
def main():
        wallet = Wallet()
        print(f'wallet.__dict__: {wallet.__dict__}')
        #Generate a signature
        data = {'foo': 'bar'}
        signature = wallet.sign(data)
        print(f'signature: {signature}')
    
if __name__ == '__main__':
        main()