# sensors

import requests
from flask import Flask, render_template, request
from flask_socketio import SocketIO
#import flask_socketio
from random import random
from threading import Lock
from datetime import datetime


thread = None
thread_lock = Lock()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'donsky!'
socketio = SocketIO(app, cors_allowed_origins='*')


def get_current_time():
    current_time = datetime.now()
    return current_time.strftime("%m/%d/%Y %H:%M:%S")


def background_thread():
    print("generating random sensor values")
    while True:
        random_sensor_value = round(random() * 100, 3)
        socketio.emit('updateSensorData', {'value': random_sensor_value, "date": get_current_time})
        socketio.sleep(1)


@app.route('/')
def index():
    return 'Rien à afficher ici'


@socketio.on('connect')
def connect():
    global thread
    print('connecté au client')
    
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(background_thread)


@socketio.on('disconnect')
def disconnect():
    print('déconnecté du client')
    
    
@app.route("/watering", methods=["POST"])
def watering():
    freq = request.json["freq"]
    if freq:
        return freq
    else:
        return "-1"


# TODO:  récupérer le délai d'envoi des données de /settings
if __name__ == "__main__":
    socketio.run(app, allow_unsafe_werkzeug=True)
    app.run(debug=True, port=5001)
