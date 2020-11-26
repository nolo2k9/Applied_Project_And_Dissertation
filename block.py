import time

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

    def __init__(self, timestamp, last_hash, hash, data):
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hash = hash
        self.data = data

    # Test
    def __repr__(self):
        # returning a formatted string containing the timestamp, last_hash, hash, data
        return (
            'Block('
            f'timestamp: {self.timestamp}, '
            f'last_hash: {self.last_hash}, '
            f'hash: {self.hash}, '
            f'data: {self.data}) '
        )

    @staticmethod
    def mine_block(last_block, data):
        """
        Adding a block to the blockchain requires computational work to be done.
        Spending cpu power = mining

        last_block used to discover the last hash value
        data is data contained within block

        Will mine a block based on the last block and data
        
        Return a new valid block based on the timestamp, last_hash, hash, data attributes
        """
        # Assinging the timestamp variable to time_ns()
        timestamp = time.time_ns()
        # last_hash is the hash of the previous block
        last_hash = last_block.hash
        # Intrim hash value
        hash = f'{timestamp}-{last_hash}'

        return Block(timestamp, last_hash, hash, data)


    @staticmethod
    def genesis():
        """
        The genesis block is the first block in a blockchain.
        It references no blocks as there are none before it.
        This method generates the genesis block
        """
        return Block(1, 'genesis_last_hash', 'There_are_none', ['A_new_birth'])


def main():
    # Experimenting adding data
    genesis_block = Block.genesis()
    block = Block.mine_block(genesis_block, 'block 1')
    print(block)


if __name__ == '__main__':
    main()
