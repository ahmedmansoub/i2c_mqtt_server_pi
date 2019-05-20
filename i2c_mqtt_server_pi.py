#!/usr/bin/python3
import paho.mqtt.client as mqtt
import time
import smbus
from time import sleep


i2c = smbus.SMBus(1)

I2C_ADD = 0x08 # Arduino I2C address


def writeI2C(data):
  i2c.write_byte(I2C_ADD, data)
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("fyp/rpi/inbox")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
	msg.payload = msg.payload.decode("utf-8")
	print(msg.payload)
	writeI2C(int (msg.payload))




client = mqtt.Client()

client.on_connect = on_connect

client.on_message = on_message
x=on_message
print(x)
client.connect("10.100.19.105", 1883, 60)

client.loop_forever()
