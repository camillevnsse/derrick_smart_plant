# sensors

import requests
import json
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from random import random
from datetime import datetime
from time import sleep
from main.db_test2 import add_data, reset_db

app = Flask(__name__)


def get_current_datetime():
    now = datetime.now()
    return now.strftime("%m/%d/%Y %H:%M:%S")
        

@app.route('/')
def index():
    return 'Rien à afficher ici'

    
@app.route("/watering", methods=["POST"])
def watering():
    freq = request.json["freq"]
    if freq:
        return freq
    else:
        return "1" # fréquence d'arrosage par défaut : tous les jours


@app.route("/data_freq", methods=["POST"])
def data_freq():
    data_freq = request.json["data_freq"]
    if data_freq:
        return data_freq
    else:
        return "1" # fréquence d'envoi des données par défaut : toutes les secondes
    


if __name__ == "__main__":
    app.run(debug=True, port=5001)

    while True:
# valeurs temporairement aléatoires : à fortiori ce sera les valeurs envoyées par les sensors
        add_data("humidity", round(random() * 100, 2), "test hum")
        add_data("temperature", round(random() * 100, 2), "test temp")
        add_data("water_lvl", round(random() * 100, 2), "test wat")
        sleep(3)
        print("e")

