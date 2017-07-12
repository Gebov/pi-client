from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
from random import randint

import time

pnConfig = PNConfiguration()
pnConfig.subscribe_key = "demo"
pnConfig.publish_key = "demo"
pubnub = PubNub(pnConfig)

def my_publish_callback(envelope, status):
    if not status.is_error():
        print("publish success")
    else:
        print("publish fail")

counter = 0
while True:
    try:
        message = "hello" + str(counter)
        pubnub.publish().channel("awesomeChannel").message(message).sync()
        time.sleep(1)
        counter+=1
    except KeyboardInterrupt:
        break
