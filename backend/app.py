from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# from endpoints import set_color, rainbow_cycle
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

if __name__ == '__main__':
    app.run('0.0.0.0')
