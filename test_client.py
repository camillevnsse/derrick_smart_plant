import json
from flask import Flask, render_template, request
from random import random
from time import sleep
# from main.db_test2 import add_data, reset_db
# from main.routes import freq as data_freq
# from main.routes import water_freq as water_freq
import requests

while True:
    print('ok')
    # valeurs temporairement aléatoires : à fortiori ce sera les valeurs envoyées par les sensors

    # TODO: faire requête post vers /add_data pour envoyer données des sensors
    hum_value = round(random() * 100, 1)
    temp_value = round(random() * 100, 1)
    water_lvl_value = round(random() * 100, 1)
    url = "http://127.0.0.1:5000/store_data"

    data = requests.post(url, json={"humidity": hum_value, "temperature": temp_value, "water_lvl": water_lvl_value})
    '''add_data("humidity", round(random() * 100, 1), "hum")
    add_data("temperature", round(random() * 100, 1), "temp")
    add_data("water_lvl", round(random() * 100, 1), "wat")'''

    sleep(3)
    print('ok2')
