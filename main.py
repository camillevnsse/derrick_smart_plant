import json
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
from watering import WateringApi
from random import random
from threading import Lock
from datetime import datetime
import db_test
import requests

app = Flask(__name__)
thread = None
thread_lock = Lock()

socketio = SocketIO(app, cors_allowed_origins='*')
app.config['SQLALCHEMY'] = "slqlite:///test_database.db"


def get_current_datetime():
    now = datetime.now()
    return now.strftime("%m/%d/%Y %H:%M:%S")


def background_thread():
    print("Generating random sensor values")
    while True:
        dummy_sensor_value = round(random() * 100, 3)
        socketio.emit('updateSensorData', {'value': dummy_sensor_value, "date": get_current_datetime()})
        socketio.sleep(1)


@app.route("/")
def home():
    dt = db_test.result
    hum = dt[0][0]
    temp = dt[0][1]
    return render_template("home.html", hum=hum, temp=temp)


@socketio.on('connect')
def connect():
    global thread
    print('Client connected')

    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(background_thread)


@socketio.on('disconnect')
def disconnect():
    print('Client disconnected', request.sid)


    @app.route("/statistics")
def statistics():
    dt = db_test.result

    return render_template("statistics.html")


@app.route("/settings", methods=["POST", "GET"])
def settings():
    if request.method == "POST":
        freq = {"freq": request.form.get("freq")}
        requests.post('http://127.0.0.1:5001/watering', json=freq)
    return render_template("settings.html")



@app.route("/city", methods=("GET", "POST"))
def get_weather():
    if request.method == "POST":
        city = request.form["city"]
        key = ''
        url_path = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=' + key

        # r = requests.get(url_path)
        # data = r.json()
        data = {'coord': {'lon': -0.1257, 'lat': 51.5085},
                'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}],
                'base': 'stations',
                'main': {'temp': 14.29, 'feels_like': 13.16, 'temp_min': 12.25, 'temp_max': 15.86, 'pressure': 1015,
                         'humidity': 53}, 'visibility': 10000, 'wind': {'speed': 4.63, 'deg': 280},
                'clouds': {'all': 100}, 'dt': 1664128421,
                'sys': {'type': 2, 'id': 2075535, 'country': 'GB', 'sunrise': 1664085064, 'sunset': 1664128404},
                'timezone': 3600, 'id': 2643743, 'name': 'London', 'cod': 200}

        return render_template("weather.html", city=city, data=data)

    return render_template("weather.html")


@app.route("/water")
def test_notif():
    WateringApi.water()
    return json.dumps({"status": 200, "notification_status": "correct"})


if __name__ == "__main__":
    app.run(debug=True)
    socketio.run(app, allow_unsafe_werkzeug=True)
