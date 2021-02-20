# MQTT Client demo
# Continuously monitor two different MQTT topics for data,
# check if the received data matches two predefined 'commands'
 
import paho.mqtt.client as mqtt
import threading
import blinkt
 
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
    # Subscribing in on_connect() - if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("BlueStar/pi")
 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

    # if msg.payload == "Hello":
        # print("Received message #1, do something")
        # Do something
	# blinkt.set_pixel(0, 255,0,255)
	# blinkt.show()

   # if msg.payload == "World!":
   #     print("Received message #2, do something else")
        # Do something else

    data = msg.payload
    if type(data) is bytes:
        data = data.decode('utf-8')
    data = data.split(':')
    command = data.pop(0)

    if (command == 'custom'):
        rgbValues = data.pop(0).split('|')
        index = 0
        for rgb in rgbValues:
            parts = rgb.split(',')
            blinkt.set_pixel(index, parts[0], parts[1], parts[2])
            index += 1
            
        blinkt.show()

    if (command == 'red'):
        for i in range(blinkt.NUM_PIXELS):
             blinkt.set_pixel(i, 255, 0, 0)
        blinkt.show()
    
    if (command == 'clear'):
        blinkt.clear()
        blinkt.show()

    if command == 'clr' and len(data) == 0:
        blinkt.clear()
        blinkt.show()
        return

    if command == 'rgb' and len(data) == 4:
        try:
            pixel = data.pop(0)

            if pixel == '*':
                pixel = None
            else:
                pixel = int(pixel)
                if pixel > 7:
                    print('Pixel out of range: ' + str(pixel))
                    return

            r, g, b = [int(x) & 0xff for x in data]

            print(command, pixel, r, g, b)

        except ValueError:
            print('Malformed command: ' + str(msg.payload))
            return

        if pixel is None:
            for x in range(blinkt.NUM_PIXELS):
                blinkt.set_pixel(x, r, g, b)
        else:
            blinkt.set_pixel(pixel, r, g, b)

        blinkt.show()
        return

# Initialise Blinkt
blinkt.set_clear_on_exit()
blinkt.set_brightness(0.05) 

# Create an MQTT client and attach our routines to it.
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
 
client.connect("test.mosquitto.org", 1883, 60)
 
# Process network traffic and dispatch callbacks. This will also handle
# reconnecting. Check the documentation at
# https://github.com/eclipse/paho.mqtt.python
# for information on how to use other loop*() functions
client.loop_forever()
