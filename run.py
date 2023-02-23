'''
import json
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
from watering import WateringApi
from random import random
from threading import Lock
from datetime import datetime
import requests
import db_test2 as dbt
'''

# initialisation de l'application flask et du thread
'''
app = Flask(__name__)
app.app_context().push()
thread = None
thread_lock = Lock()

socketio = SocketIO(app, cors_allowed_origins='*')

# récupérer la date actuelle
def get_current_datetime():
    now = datetime.now()
    return now.strftime("%m/%d/%Y %H:%M:%S")


# récupérer les dernières valeurs de la base de données et les émettre pour les afficher dans "statistiques"
def background_thread():
    print("Generating random sensor values")
    hum_init = [dbt.hum_values[-i].values for i in range(1, 11)]
    temp_init = [dbt.temp_values[-i].values for i in range(1, 11)]
    wat_init = [dbt.wat_values[-i].values for i in range(1, 11)]
    hum_init.reverse()
    temp_init.reverse()
    wat_init.reverse()

    for i in range (10):
        socketio.emit('updateSensorData', {"hum_value": hum_init[i], "temp_value": temp_init[i], "wat_value": wat_init[i], "date": get_current_datetime(), "animation": 'none'})

    socketio.sleep(2)

    while True:
        dummy_sensor_value = round(random() * 100, 3)
        #dummy_sensor_value = {}
        humidity = dbt.hum_values[-1].values
        temperature = dbt.temp_values[-1].values
        water_lvl = dbt.wat_values[-1].values

        socketio.emit('updateSensorData', {'hum_value': humidity, "temp_value": temperature, "wat_value": water_lvl , "date": get_current_datetime(), "animation": ''})
        socketio.sleep(2)
        
        # @luc : il faudrait que les valeurs soient les dernières de la db
        # @luc : il faut que tu fasses le truc de l'initialisation où ça push les 10 dernières valeurs de la db
        # on va emit dans un dictionnaire {"humidity": float, "temperature": float, "niveau eau": float, "date": string}



# page d'accueil
@app.route("/")
def home():
    hum = dbt.hum_values[-1].values
    print(dbt.get_last_data("humidity"))
    temp = dbt.temp_values[-1].values
    return render_template("home.html", hum=hum, temp=temp)


# connexion au client pour le socket
@socketio.on('connect')
def connect():
    global thread
    print('Client connected')

    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(background_thread)

# déconnexion du client
@socketio.on('disconnect')
def disconnect():
    print('Client disconnected', request.sid)


# paramètres : régler la fréquence d'arrosage et fréquence d'envoi des données
@app.route("/settings", methods=["POST", "GET"])
def settings():
    if request.method == "POST":
        freq = {"freq": request.form.get("freq")}
        requests.post('http://127.0.0.1:5001/watering', json=freq)
    return render_template("settings.html")


@app.route("/statistics")
def statistics():
    return render_template("statistics.html")


@app.route("/weather", methods=("GET", "POST"))
def get_weather():
    return render_template("weather.html")


@app.route("/water")
def test_notif():
    WateringApi.water()
    return json.dumps({"status": 200, "notification_status": "correct"})
'''


from main import app, socketio

if __name__ == "__main__":
    app.run(debug=True, port=5000)
    socketio.run(app, allow_unsafe_werkzeug=True)
