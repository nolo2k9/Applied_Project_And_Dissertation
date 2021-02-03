import time
from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback

pnconfig = PNConfiguration()
#Subscribe key
pnconfig.subscribe_key = "sub-c-3d41238a-4435-11ea-afa6-0abb81b5425e"
#Publish key
pnconfig.publish_key = "pub-c-cf24a228-2121-4227-8fd2-e3c00c9c63a9"
pubnub = PubNub(pnconfig)
#Experiment data
TEST_CHANNEL = 'TEST_CHANNEL'


class Listener(SubscribeCallback):
    #Subscribe to message channel
    def message(self,pubnub,message_object):
        print(f'\n-- Channel:  {message_object.channel} | Message: {message_object.message}')

class PubSub():
    """
    Handles publish subscribe layer of application
    Provides communication between nodes in the blockchain network
    """
    def __init__(self):
        self.pubnub = PubNub(pnconfig)
        #Subscribe to test channel
        self.pubnub.subscribe().channels([TEST_CHANNEL]).execute()
        #Listen for incoming messages
        self.pubnub.add_listener(Listener())
        
    def publish(self, channel, message):
        """
        Publish the message object to channel
        """
        #Publish message to channel
        self.pubnub.publish().channel(channel).message(message).sync()
    


def main():
    pubsub = PubSub()
    #Ensures that the publish channel is ran after the subscribe (avoids a race )
    time.sleep(1)
    pubsub.publish(TEST_CHANNEL, {'foo': 'bar'})
    
    
if __name__ == '__main__':
    main()
    

    

    



