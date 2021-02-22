from backend.blockchain.block import Block
from backend.wallet.transaction import Transaction
from backend.config import MINING_REWARD_INPUT

class Blockchain:
    """
    This class contains the code for the blockchain.
    A blockchain is a public ledger that contains transactional data.
    These transactions are implemented as a list of blocks.
    Blocks are data sets of transactions.
    """
    # init method

    def __init__(self):
        # Every blockchain instance will contain a chain attribute implemented as a list. The list will be a list of blocks,consisting of block items
        # Setting genesis to be the first block of the chain
        self.chain = [Block.genesis()]

    # Method to enable the blockchain to add blocks
    def add_block(self, data):
        # self.chain[-1] refers to the last block at the index of -1
        # blocks are added using mine_block
        # append this block and data to the chain
        self.chain.append(Block.mine_block(self.chain[-1], data))
    # Test

    def __repr__(self):
        # returning a formatted string containing the local chain list
        return f'Blockchain: {self.chain}'

    def replace_chain(self, chain):
        """
        This method replaces the current chain with an incoming one, but only if the following requirements are met:
        - The new chain must be longer than the local one.
        - The new chain is in the correct format
        """
        # if the new chain is <= current chain raise an exception
        if len(chain) <= len(self.chain):
            raise Exception(
                'Current chain cannot be replaced: The incoming chain must be longer.')
        # Calling the isValidChain method to ensure requirements are met
        try:
            Blockchain.isValidChain(chain)

        except Exception as e:
            raise Exception(
                f'Current chain cannot be replaced: The incoming chain must be correctly formatted: {e}')
        # If everything is correct assign the current chain to the new chain
        self.chain = chain

    def to_json(self):
        """
        Serialize the blockchain into a list of blocks
        """
        return list(map(lambda block: block.to_json(), self.chain))

    @staticmethod
    def from_json(chain_json):
        """
        Deserialize a list of serialized blocks into a Blockchain instance.
        The result will contain a chain list of block instances.
        """

        blockchain = Blockchain()
        blockchain.chain = list(
            # transforms jsonified block data
            map(lambda block_json: Block.from_json(block_json), chain_json)
        )

        return blockchain

    @staticmethod
    def isValidChain(chain):
        """
        This method validates incoming chains and enforces the following rules:
        - Chains must start with the genesis block.
        - Blocks must be formatted correctly
        """
        # Check to ensure the genesis block is valid
        if chain[0] != Block.genesis():
            raise Exception('The genesis block must be valid')

        # Loop through the blocks in the chain
        for i in range(1, len(chain)):
            block = chain[i]
            # Last block is previous element
            last_block = chain[i-1]
            # Check conditions laid out in isValidBlock
            Block.isValidBlock(last_block, block)

    @staticmethod
    def is_valid_transaction_chain(chain):
        """
        Enforces chain transaction boundaries.
        - Transactions must unique
        - Must only be one mining reward for mining a block
        - Every transaction must be valid
        """
        # Set of transaction id's
        transaction_ids = set()
        # For each block in the chain
        for block in chain:
            #Control mining reward
            has_mining_reward = False
            """
            Iterate through each transaction in this blocks data
            Blocks consist of json representations of each transaction
            Calling each item in the block data
            """
            #Process that transactions json
            for transaction_json in block.data: 
                #https://stackoverflow.com/questions/6578986/how-to-convert-json-data-into-a-python-object
                transaction = Transaction.from_json(transaction_json)
                
                if transaction.input == MINING_REWARD_INPUT:
                    #If already true
                    if has_mining_reward:
                        raise Exception ('Only one mining reward per block is allowed.'\
                            f'Check the followig block hash: {block.hash}'
                            )
                    #Set to true
                    has_mining_reward = True
                    
                #Enforcing unique transactions
                if transaction.id in transaction_ids:
                    #Show exception
                    raise Exception(f'Transaction: {transaction.id}. This transaction is not unique')
                
                #If transaction is unique add it to the set of transactions
                transaction_ids.add(transaction.id)
                Transaction.is_valid_transaction(transaction)
                    
                


def main():
    # Experimenting adding blocks
    blockchain = Blockchain()
    blockchain.add_block('One')
    blockchain.add_block('Two')
    blockchain.add_block('Three')

    print(blockchain)
    print(f'blockchain.py __name__:{__name__}')


if __name__ == '__main__':
    main()
