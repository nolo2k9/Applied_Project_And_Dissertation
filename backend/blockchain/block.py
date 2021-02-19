import time
from backend.utils.hashing import crypto_hash  # hash function
from backend.utils.hex_to_binary import hex_to_binary  # hex_to_binary function
from backend.config import MINE_RATE

# Global variable GENESIS_DATA
# GENESIS_DATA dictionary
GENESIS_DATA = {
    'timeStamp': 1,
    'last_hash': 'genesis_last_hash',
    'hash': 'genesis_hash',
    'data': [],
    'difficulty': 5,
    'nonce': 'genesis_nonce'
}


class Block:
    """
    Unit of storage.
    Store transactional data in the blockchain which supports a cryptocurrency.
    """

    '''
    Each block has the following attributes:
    timestamp: Created using a time module in python
    last_hash: Hash of the previous block
    hash: Hash of the block itself
    data: The data being stored
    '''
    # init (constructor)mmethod containing the timestamp, last_hash, hash, data

    def __init__(self, timestamp, last_hash, hash, data, difficulty, nonce):
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hash = hash
        self.data = data
        self.difficulty = difficulty
        self.nonce = nonce

    # Test
    def __repr__(self):
        # returning a formatted string containing the timestamp, last_hash, hash, data
        return (
            'Block('
            f'timestamp: {self.timestamp}, '
            f'last_hash: {self.last_hash}, '
            f'hash: {self.hash}, '
            f'data: {self.data}, '
            f'difficulty: {self.difficulty}, '
            f'nonce: {self.nonce}) '
        )

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def to_json(self):
        """
        Serialize the block into a dicionary representation
        """
        return self.__dict__

    @staticmethod
    def mine_block(last_block, data):
        """
        Adding a block to the blockchain requires computational work to be done.
        Spending cpu power = mining

        last_block used to discover the last hash value
        data is data contained within block

        Will mine a block based on the last block and data, until a block hash is found that meets the leading 0's proof of work

        Return a new valid block based on the timestamp, last_hash, hash, data attributes
        """
        # Assinging the timestamp variable to time_ns()
        timestamp = time.time_ns()
        # last_hash is the hash of the previous block
        last_hash = last_block.hash
        # Setting the difficulty for new blocks to depend on the change_difficulty()
        difficulty = Block.change_difficulty(last_block, timestamp)
        # Settting nonce to zero
        nonce = 0
        # Intrim hash value
        hash = crypto_hash(timestamp, last_hash, data,
                           difficulty, nonce)  # hash function called in

        """
        Loop until a hash value is found where a sub-string is found that equals 0 * difficulty
        Will generate a string with the proper number of leading zeros.
        Find a hash that will meet the proof of work requirement
        Eventually the hash will lead with the correct number of leading zeros
        When the correct nonce is found the loop will be broken 
        Then a new block will be returned
        """
        while hex_to_binary(hash)[0:difficulty] != '0' * difficulty:  # hash is converted here using hex_to_binary imported function
            # Add one to the nonce value
            nonce += 1

            # Regenerate timestamp to have to most accurate value possible as it could take a while to find a correct number of zeros
            timestamp = time.time_ns()
            # Setting the difficulty for new blocks to depend on the change_difficulty()
            difficulty = Block.change_difficulty(last_block, timestamp)
            # Regnerate the hash inputs
            hash = crypto_hash(timestamp, last_hash, data, difficulty, nonce)

        return Block(timestamp, last_hash, hash, data, difficulty, nonce)

    @staticmethod
    def genesis():
        """
        The genesis block is the first block in a blockchain.
        It references no blocks as there are none before it.
        This method generates the genesis block
        """
        return Block(

            GENESIS_DATA['timeStamp'],
            GENESIS_DATA['last_hash'],
            GENESIS_DATA['hash'],
            GENESIS_DATA['data'],
            GENESIS_DATA['difficulty'],
            GENESIS_DATA['nonce']
        )

    @staticmethod
    def from_json(block_json):
        """
        This method will deserialize a blocks json representation back into a block instance.
        """
        return Block(**block_json)

    @staticmethod
    def change_difficulty(last_block, new_timestamp):
        """
        Method to calculate the adjusted difficulty according to the set MINE_RATE
        If the last block is mined faster than the MINE_RATE it will increase the difficulty and make it more difficult for the next block.
        If the last block is mined slower than the MINE_RATE it will decrease the difficulty and make it less diffiult for the next block.
        Default of 1 
        """

        """
        Checking the timestamp of the previous block
        If the value of the new_timestamp - last_block.last_block.timestamp is less than the MINE_RATE
        Increase the difficulty by 1 otherwise knock 1 off the difficulty
        """
        if(new_timestamp - last_block.timestamp) < MINE_RATE:
            return last_block.difficulty + 1

        if(last_block.difficulty - 1) > 0:
            return last_block.difficulty - 1

        return 1

    @staticmethod
    def isValidBlock(last_block, block):
        """
        This method validates a block by:
        - The block must have the correct last hash reference
        - The block must have the correct number of leading zeros according to the difficulty of the hash (proof of work requirements)
        - The difficulty must only be adjusted by 1
        - The block hash must be a valid combination of the block fields
        """
        # if this blocks lash hash is not the same as the one before it raise an exception
        if block.last_hash != last_block.hash:

            raise Exception('The blocks lash_hash must be correct')

        # if the difficulty is not the same raise an exception
        "Wrapped in a call to hext to binary as its calling on the binary representation rather than the original hex representation"
        if hex_to_binary(block.hash)[0:block.difficulty] != '0' * block.difficulty:
            raise Exception(
                'The correct proof of work requirement was not met')

        "Check that the difficulty is only being adjusted by one"
        # check the difference between the difficulty of the last block and the current difficulty
        # get absolute value of the difference
        if abs(last_block.difficulty - block.difficulty) > 1:
            raise Exception('Block difficulty must only be adjusted by one')

        # variable: reconstructed hash
        reconstructed_hash = crypto_hash(
            block.timestamp,
            block.last_hash,
            block.data,
            block.nonce,
            block.difficulty
        )

        if block.hash != reconstructed_hash:
            raise Exception(
                'Block hash must be correct: Block hash must be a valid combination of the block fields')


def main():
    genesis_block = Block.genesis()
    bad_block = Block.mine_block(Block.genesis(), 'foo')
    bad_block.last_hash = 'evil_data'
    try:
        Block.isValidBlock(genesis_block, bad_block)
    except Exception as e:
        print(f'is_valid_block: {e}')


if __name__ == '__main__':
    main()
