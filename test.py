import paho.mqtt.client as mqtt
import time


def on_connect(client, userdata, flags, rc):
    print(rc)
    client.subscribe("2")

#def on_message(client, userdata, msg):
#    print(msg.topic+" "+str(msg.payload))

def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)

#host="1.1.1.1"
host = "97c3ce89f18b4804a85b36cb595845a9.s2.eu.hivemq.cloud"

client = mqtt.Client("P1")
#client.username_pw_set(username = "ibishu", password="kalimanjaro228")
#client.on_connect = on_connect
client.on_message = on_message
client.connect(host, port=8883, keepalive=60, bind_address="")

client.loop_start()
client.subscribe("2")
print("Publishing message to topic","house/bulbs/bulb1")
client.publish("2","hello")
time.sleep(4)
client.loop_stop()
#client.loop_forever()


