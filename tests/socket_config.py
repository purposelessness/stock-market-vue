import time

import socketio


def prepare_controller():
    sio = socketio.Client()

    @sio.on('connect', namespace='/controller')
    def connect():
        sio.emit('stopClock', {}, namespace='/controller')
        sio.emit('setDate', '2020-10-12', namespace='/controller')
        sio.emit('setClockDelay', '1000', namespace='/controller')
        sio.emit('startClock', namespace='/controller')

    sio.connect('http://localhost:3000', namespaces=['/controller'])

    time.sleep(1)

    sio.disconnect()


def reset_controller():
    sio = socketio.Client()

    @sio.on('connect', namespace='/controller')
    def connect():
        sio.emit('stopClock', {}, namespace='/controller')

    sio.connect('http://localhost:3000', namespaces=['/controller'])

    time.sleep(1)

    sio.disconnect()

