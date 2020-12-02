import time
from backend.utils.hashing import crypto_hash  # hash function

#Global variable GENESIS_DATA
#GENESIS_DATA dictionary
GENESIS_DATA = {
    'timeStamp': 1,
    'last_hash': 'genesis_last_hash',
    'hash': 'genesis_hash',
    'data': [],
    'difficulty': 3,
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
        # Setting the difficulty for new blocks to that of the previous block
        difficulty = last_block.difficulty
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
        while hash[0:difficulty] != '0' * difficulty:
            # Add one to the nonce value
            nonce += 1

            # Regenerate timestamp to have to most accurate value possible as it could take a while to find a correct number of zeros
            timestamp = time.time_ns()

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
      


def main():
    # Experimenting adding data
    genesis_block = Block.genesis()
    block = Block.mine_block(genesis_block, 'block 1')
    print(block)


if __name__ == '__main__':
    main()
