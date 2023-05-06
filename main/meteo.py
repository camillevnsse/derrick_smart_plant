# récupérer les données météorologiques

from flask import render_template, request, send_file, make_response
from main import app, socketio
import requests as req
import json
import dotenv, os
from math import pow

dotenv.load_dotenv()
TOKEN_API_METEO=os.getenv("TOKEN_API_METEO")

with open("data/correspondances_codes.json","rb") as file:
    correspondances_api = json.loads(file.read().decode("utf-8"))

def refresh(insee):
    Resp = req.get(f'https://api.meteo-concept.com/api/forecast/nextHours?token={TOKEN_API_METEO}&insee={insee}')
    Data = json.loads(Resp.text)
    return Data

def correspondance(code) -> list:
    return correspondances_api.get(str(code),[])

@app.route("/weather", methods=["GET"])
def get_weather():
    code_ville = request.args.get("insee", False)
    if code_ville:
        #recuperons la reponse de l'api
        meteo = refresh(code_ville)

        #on récupère les previsions
        data = meteo.get("forecast", [])[0]
        #on ajoute le nom de la ville
        data["name"] = meteo.get('city', {}).get("name", None)
        #ici on ajoute le code d'image
        code_meteo = data["weather"]
        data["correspondance"] = correspondance(code_meteo)
        #temperature ressentie selon : https://www.alpiniste.fr/out/pictures/wysiwigpro/kalkulatoren/js/windchill-logic.js
        temp = data["temp2m"]
        if -50 < temp < 50:
            windchillTemperature = 13.12 + (0.6215*data["temp2m"]) - (11.37 * pow(data["wind10m"],0.16)) + (0.3965 * data["temp2m"] * pow(data["wind10m"],0.16))
            windchillTemperature = round(windchillTemperature, 1)
            data["temp_ressentie"] = str(windchillTemperature)
        else:
            data["temp_ressentie"] = ""
        

        data1 = {'coord': {'lon': -0.1257, 'lat': 51.5085},
                'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}],
                'base': 'stations',
                'main': {'temp': 14.29, 'feels_like': 13.16, 'temp_min': 12.25, 'temp_max': 15.86, 'pressure': 1015,
                         'humidity': 53}, 'visibility': 10000, 'wind': {'speed': 4.63, 'deg': 280},
                'clouds': {'all': 100}, 'dt': 1664128421,
                'sys': {'type': 2, 'id': 2075535, 'country': 'GB', 'sunrise': 1664085064, 'sunset': 1664128404},
                'timezone': 3600, 'id': 2643743, 'name': code_ville, 'cod': 200}

        return render_template("weather.html", city=code_ville, data=data)
    return render_template("weather.html")

@app.route("/cities")
def donner_villes():
    return send_file(os.path.join(os.getcwd(), "data/donnees_villes_france.json"), mimetype="application/json")
