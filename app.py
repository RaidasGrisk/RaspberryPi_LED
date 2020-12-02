from flask import Flask
app = Flask(__name__)

from endpoints import set_color, rainbow_cycle
from flask import request


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/set_color')
def set_color_ep(r=255, g=0, b=0):
    r = request.args.get('r', r)
    g = request.args.get('g', g)
    b = request.args.get('b', b)
    set_color((int(r), int(g), int(b)))
    return 'done!'

@app.route('/rainbow')
def set_color_rainbow(wait=0.01):
    wait = request.args.get('wait', wait)
    rainbow_cycle(float(wait))
    return 'done!'


# scp /home/raidas/Desktop/RaspberryPi_LED/* pi@192.168.43.195:/home/pi/RaspberryPi_LED
# sudo flask run --host=0.0.0.0