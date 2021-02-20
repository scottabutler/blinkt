from flask import Flask, render_template, url_for, redirect, request
import paho.mqtt.publish as publish

app = Flask(__name__)

Items = ["red", "clear"]

@app.route('/')
def index():
    return render_template('index_custom.html', len=len(Items), Items = Items)

@app.route('/publish/<cmd>')
def pub(cmd):
    allowed_commands = ["red", "clear"]
    if (cmd in allowed_commands):
        publish.single("BlueStar/pi", cmd, hostname="test.mosquitto.org")
    return redirect(url_for('index'))

@app.route('/publish/custom')
def custom():
    hexColours = request.args.get("c").split(",")
    rgbColours = [];
    for h in hexColours:
        rgbColours.append(hex_to_rgb(h))
        
    publish.single("BlueStar/pi", "custom:" + "|".join(rgbColours), hostname="test.mosquitto.org")
    return redirect(url_for('index'))
    
def hex_to_rgb(hex):
    if (len(hex) == 3):
        return str(int(hex[0:1], 16)) + "," + str(int(hex[1:2], 16)) + "," + str(int(hex[2:3], 16))
    elif (len(hex) == 6):
        return str(int(hex[0:2], 16)) + "," + str(int(hex[2:4], 16)) + "," + str(int(hex[4:6], 16))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
