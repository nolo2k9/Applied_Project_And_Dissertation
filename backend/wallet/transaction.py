import uuid
import time
from backend.wallet.wallet import Wallet
class Transaction:
    """
    Store an exchange of currency from the sender to one or more recipients.
    """
    
    def __init__(self, sender_wallet, recipient, amount):
        """
        The sender wallet represents an instance of the sender wallets class.
        A sign method will be used to generate a signature for a transaction.
        
        The recipient is another wallets address string. 
        
        The amount is the amount of currency being exchanged.
        """
        """
        Transaction id
        Once transactions are recorded into the blockchain it ensures transactions arent duplicated
        By preventing a transaction with the same id from being recorded. 
        Will help searching for a transaction in the long list of recorded trasnactions on the blockchain.
        """
        #Get the first 8 characters from generated uuid 
        self.id = str(uuid.uuid4())[0:8]
        #Output records who the recipients of the transaction are and how much currency is being recieved from the transaction
        self.output = self.create_output(sender_wallet, recipient, amount)
        #Input receives metadata about the transaction such as the timestamp, the senders address, the public key and transaction signature
        self.input = self.create_input(sender_wallet, self.output)
        
    def create_output(self, sender_wallet, recipient, amount):
                """
                Structures the output data for the tansaction.
                """
                #If the amount being sent is > than the wallet holders currenct balance
                if amount > sender_wallet.balance:
                    raise Exception('You dont hold enough Delta Coin to make this trasaction')
                #Output dictionary
                output = {}
                output[recipient] = amount
                #Take the amount being sent from the sender wallets total amount
                output[sender_wallet.address] = sender_wallet.balance - amount
                
                return output
            
            
    def create_input(self, sender_wallet, output):
                """
                Structure the input data for the transaction.
                Sign the transaction also includes the senders public key and their address
                """
                return{
                    
                    'timestamp': time.time_ns(),
                    'amount': sender_wallet.balance,
                    'address': sender_wallet.address,
                    'public_key': sender_wallet.public_key,
                    'signature' : sender_wallet.sign(output)
                }
    
    def update(self, sender_wallet,recipient, amount):
        """
        Updates transactions with an existing or new recipient.
        """
        # Check to see if the amount being sent is greater than the holders balance
        if amount > self.output[sender_wallet.address]:
            raise Exception('Amount exceeds balance')
        
        if recipient in self.output:
            # Add the new amount being sent to the recipient
            self.output[recipient] = self.output[recipient] + amount
            
        else: 
            self.output[recipient] = amount
            
        self.output[sender_wallet.address] = self.output[sender_wallet.address] - amount
        
        #Resign the transaction.
        
        self.input = self.create_input(sender_wallet, self.output)
        
            
            
    @staticmethod
    def is_valid_transaction(transaction):
        """
        This method:
        Validates valid transactions.
        Raises an exception if  transaction is invalid.]
        """
        
        output_total = sum(transaction.output.values())
        
        if transaction.input['amount'] != output_total:
            raise Exception('Invalid transaction output values')
        
        #Check if the transaction signature is invalid
        if not Wallet.verify(
            transaction.input['public_key'],
            transaction.output,
            transaction.input['signature']
        ):
            raise Exception('Invalid signature')
                    
def main():
    transaction = Transaction(Wallet(), 'recipient', 15)
    print(f'transaction.__dict__: {transaction.__dict__}')

if __name__ == '__main__':
    main()
    
        
    
        