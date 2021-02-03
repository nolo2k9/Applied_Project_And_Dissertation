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
#Send network request
pubnub.subscribe().channels([TEST_CHANNEL]).execute()

class Listener(SubscribeCallback):
    #Subscribe to message channel
    def message(self,pubnub,message_object):
        print(f'\n-- Incoming message_object:  {message_object}')
#Listen for incoming messages
pubnub.add_listener(Listener())


def main():
    #Ensures that the publish channel is ran after the subscribe (avoids a race )
    time.sleep(1)
    #Publish message to channel
    pubnub.publish().channel(TEST_CHANNEL).message({'foo': 'bar'}).sync()
    
if __name__ == '__main__':
    main()
    

    

    



