from bottle import get, run, template
from bottle.ext.websocket import GeventWebSocketServer
from bottle.ext.websocket import websocket
import time

@get('/')
def index():
    return template('./view/index.html')

seq=1

@get('/websocket', apply=[websocket])
def echo(ws):
    global seq
    while True:
        ws.send("Get"+str(seq))
        seq+=1
        time.sleep(1)

run(host='localhost', port=8001, server=GeventWebSocketServer)