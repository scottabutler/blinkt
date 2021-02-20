# MQTT Publish Demo
# Publish two messages, to two different topics

import paho.mqtt.publish as publish

publish.single("BlueStar/pi", "rgb,3,123,5,23", hostname="test.mosquitto.org")
print("Done")