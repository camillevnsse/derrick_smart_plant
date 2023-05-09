# code micropython pour l'envoi des données des capteurs au serveur web
import urequests as requests
import time
import machine
from random import random

url = 'http://192.168.0.40:5000/store_data'


def debug(text, url):
    headers = {'Content-Type': 'application/json'}
    data = '{"text": "' + f"{text}" + '"}'
    req = requests.post(url, data=data, headers=headers)


led = machine.Pin(2, machine.Pin.OUT)

# Configuration des broches pour les entrées/sorties
pin_S0 = machine.Pin(14, machine.Pin.OUT)  # D5
pin_S1 = machine.Pin(12, machine.Pin.OUT)  # D6
pin_S2 = machine.Pin(13, machine.Pin.OUT)  # D7
pin_A0 = machine.ADC(0)


# Fonction pour sélectionner l'entrée Y1
def select_Y1():
    pin_S0.value(1)
    pin_S1.value(0)
    pin_S2.value(0)


# Fonction pour sélectionner l'entrée Y2
def select_Y2():
    pin_S0.value(0)
    pin_S1.value(1)
    pin_S2.value(0)


while True:
    try:
        debug('Start', url)
        led.value(0)

        # Récupération de l'humidité du sol
        select_Y1()
        humidity = pin_A0.read()
        debug(humidity, url)

        # Récupération du niveau d'eau
        select_Y2()
        water_level = pin_A0.read()
        debug(water_level, url)

        # Génération d'une valeur aléatoire de température, remplace la valeur du DHT11
        temperature = round(random() * 100, 1)
        debug(temperature, url)

        r = requests.post(url, json={"humidity": humidity, "temperature": temperature, "water_lvl": water_level})
        time.sleep(1)
        led.value(1)
        time.sleep(9)
        debug('end', url)
    except Exception as err:
        data = f"{type(err).__name__} was raised {err}"
        debug(data, url)
