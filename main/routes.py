import json
from flask import render_template, request
from main import app, socketio
import main.db_test2 as dbt
from main.watering import WateringApi
from threading import Lock
from datetime import datetime
from random import random
import requests


thread = None
thread_lock = Lock()

# récupérer la date actuelle
def get_current_datetime():
    now = datetime.now()
    return now.strftime("%m/%d/%Y %H:%M:%S")


# récupérer les dernières valeurs de la base de données et les émettre pour les afficher dans "statistiques"
def background_thread():
    app.app_context().push()

    print("Generating random sensor values")
    while True:
        humidity = dbt.get_last_data("humidity", 1)[0]
        temperature = dbt.get_last_data("temperature", 1)[0]
        water_lvl = dbt.get_last_data("water_lvl", 1)[0]

        socketio.emit('updateSensorData', {'hum_value': humidity, "temp_value": temperature, "wat_value": water_lvl , "date": get_current_datetime(), "animation": ''})
        print("e")
        socketio.sleep(3)
        
        # @luc : il faudrait que les valeurs soient les dernières de la db
        # @luc : il faut que tu fasses le truc de l'initialisation où ça push les 10 dernières valeurs de la db
        # on va emit dans un dictionnaire {"humidity": float, "temperature": float, "niveau eau": float, "date": string}


# page d'accueil
@app.route("/")
def home():
    hum = dbt.get_last_data("humidity", 1)[0]
    temp = dbt.get_last_data("temperature", 1)[0]
    return render_template("home.html", hum=hum, temp=temp)


# connexion au client pour le socket
@socketio.on('connect')
def connect():
    global thread
    print('Client connected')
    hum_init = dbt.get_last_data("humidity", 10)
    temp_init = dbt.get_last_data("temperature", 10)
    wat_init = dbt.get_last_data("water_lvl", 10)
    hum_init.reverse()
    temp_init.reverse()
    wat_init.reverse()

    for i in range (10):
        socketio.emit('updateSensorData', {"hum_value": hum_init[i], "temp_value": temp_init[i], "wat_value": wat_init[i], "date": get_current_datetime(), "animation": 'none'})

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