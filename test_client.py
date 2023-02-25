import json
from flask import Flask, render_template, request
from random import random
from time import sleep
from main.db_test2 import add_data, reset_db
from main.routes import freq as data_freq
from main.routes import water_freq as water_freq


while True:
    # valeurs temporairement aléatoires : à fortiori ce sera les valeurs envoyées par les sensors
    add_data("humidity", round(random() * 100, 1), "test hum")
    add_data("temperature", round(random() * 100, 1), "test temp")
    add_data("water_lvl", round(random() * 100, 1), "test wat")

    sleep(3)

    '''if data_freq:
        sleep(data_freq)
    else:
        sleep(3)'''
