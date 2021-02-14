import uuid
from backend.config import STARTING_BALANCE

from cryptography.hazmat.backends import default_backend

#Eliptic cryptography module 
from cryptography.hazmat.primitives.asymmetric import ec

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
        
        
def main():
        wallet = Wallet()
        print(f'wallet.__dict__: {wallet.__dict__}')
    
if __name__ == '__main__':
        main()