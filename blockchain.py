class Block:
    """
    Unit of storage.
    Store transactional data in the blockchain which supports a cryptocurrency.
    """
    
    #init method
    def __init__(self, data):
       #Each block will contain a data attribute. The data come in from the init method
       self.data = data
    
    #Test
    def __repr__(self):
        #returning a formatted string containing the data
        return f'Block - data: {self.data}'
       
    
class Blockchain:
    """
    This class contains the code for the blockchain.
    A blockchain is a public ledger that contains transactional data.
    These transactions are implemented as a list of blocks.
    Blocks are data sets of transactions.
    """
    #init method
    def __init__(self):
       #Every blockchain instance will contain a chain attribute implemented as a list. The list will be a list of blocks,consisting of block items
       self.chain = []
       
    #Method to enable the blockchain to add blocks
    def add_block(self, data):
        #instance of block class containing the data
        #append this block and data to the chain
       self.chain.append(Block(data))
    #Test
    def __repr__(self):
        #returning a formatted string containing the local chain list
        return f'Blockchain: {self.chain}'

# Experimenting adding blocks
blockchain = Blockchain()
blockchain.add_block('One')
blockchain.add_block('Two')
blockchain.add_block('Three')

print(blockchain)
        
       