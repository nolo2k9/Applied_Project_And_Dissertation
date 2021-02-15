import uuid
import json
from backend.config import STARTING_BALANCE

from cryptography.hazmat.backends import default_backend

# Eliptic cryptography module
from cryptography.hazmat.primitives.asymmetric import ec
# Import hashing implmentation
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature


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
        # Wallet balance
        self.balance = STARTING_BALANCE
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

    @staticmethod
    def verify(public_key, data, signature):
        """
        This method verify's a signature based on the wallets public and data.
        """
        try:
            public_key.verify(signature, json.dumps(
                data).encode('utf-8'), ec.ECDSA(hashes.SHA256()))
            return True
        # catch Invalid Signature exception
        except InvalidSignature:
            return False


def main():
    wallet = Wallet()
    print(f'wallet.__dict__: {wallet.__dict__}')
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
