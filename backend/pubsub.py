import time
from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback

from backend.blockchain.block import Block

pnconfig = PNConfiguration()
#Subscribe key
pnconfig.subscribe_key = "sub-c-3d41238a-4435-11ea-afa6-0abb81b5425e"
#Publish key
pnconfig.publish_key = "pub-c-cf24a228-2121-4227-8fd2-e3c00c9c63a9"
pubnub = PubNub(pnconfig)

# Dictionary of channels
CHANNELS = {
    'TEST':'TEST',
    'BLOCK':'BLOCK'
}


class Listener(SubscribeCallback):
    def __init__(self, blockchain):
        self.blockchain = blockchain

    #Subscribe to message channel
    def message(self, pubnub, message_object):
        print(f'\n-- Channel:  {message_object.channel} | Message: {message_object.message}')

        if message_object.channel == CHANNELS['BLOCK']:
            block = Block.from_json(message_object.message)
            potential_chain = self.blockchain.chain[:] #temp chain that passes in a copy of the list
            potential_chain.append(block)

            try:
                self.blockchain.replace_chain(potential_chain)
                print('\n -- Successfully replaced the local chain')
            except Exception as e:
                print(f'\n -- Did not replace chain: {e}')

"""
Handles publish subscribe layer of application
Provides communication between nodes in the blockchain network
"""
class PubSub():
    def __init__(self, blockchain):
        self.pubnub = PubNub(pnconfig)
        #Subscribe to test channel
        self.pubnub.subscribe().channels(CHANNELS.values()).execute() # passes in our dictionary
        #Listen for incoming messages
        self.pubnub.add_listener(Listener(blockchain))
        
    """
    Publish the message object to channel
    """
    def publish(self, channel, message):
        #Publish message to channel
        self.pubnub.publish().channel(channel).message(message).sync()

    """
    Broadcast a block object to all nodes
    """
    def broadcast_block(self, block):
        self.publish(CHANNELS['BLOCK'], block.to_json())


def main():
    pubsub = PubSub() #pylint: disable=no-value-for-parameter #fixes pylint related error
    #Ensures that the publish channel is run after the subscribe (avoids a race )
    time.sleep(1)
    pubsub.publish(CHANNELS['TEST'], {'foo': 'bar'})
    
    
if __name__ == '__main__':
    main()
    

    

    



