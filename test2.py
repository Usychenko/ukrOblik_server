from mongo/mongo import get_database
import paho.mqtt.client as paho #import the client1
import time
from paho import mqtt
############


def on_message(client, userdata, message):
    print("message received " ,message.payload.decode("utf-8"))
    #i = time.time()


    i = 1

    f = open("char" + str(i) + ".json", "w")
    f.write(message.payload.decode("utf-8"))
    ####################
    db = get_database()
    new_coll =  db.my_ip  #coll = collection

    ####################

    f.close()
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
#######################################
#broker_address="iot.eclipse.org"
broker_address = "97c3ce89f18b4804a85b36cb595845a9.s2.eu.hivemq.cloud"
client = paho.Client(client_id="", userdata = None, protocol = paho.MQTTv5 )

client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)

client.username_pw_set(username = "ibishu", password = "kalimanjaro228")

print("creating new instance")

client.on_message=on_message #attach function to callback
print("connecting to broker")

client.connect(broker_address, 8883) #connect to broker



print("Subscribing to topic","house/bulbs/bulb1")
client.subscribe("2")
print("Publishing message to topic","house/bulbs/bulb1")
#client.publish("2","OFF")
#time.sleep(1) # wait
#client.loop_stop()#stop the loop
client.loop_forever()
