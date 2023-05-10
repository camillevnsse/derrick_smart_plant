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

def refresh(insee) -> dict:
    Resp = req.get(f'https://api.meteo-concept.com/api/forecast/nextHours?token={TOKEN_API_METEO}&insee={insee}')
    Data = json.loads(Resp.text)
    return Data

def correspondance(code) -> list:
    return correspondances_api.get(str(code),[])

@app.route("/weather", methods=["GET"])
def get_weather():
    code_ville = request.args.get("insee", False)
    if code_ville:
        #recupere la reponse de l'api
        meteo = refresh(code_ville)

        #je récupère les previsions
        data = meteo.get("forecast", [])[0]

        #j' ajoute le nom de la ville
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
        

        data1 = {'city': {'insee': '78117', 'cp': 78530, 'name': 'Buc', 'latitude': 48.7718, 'longitude': 2.1239, 'altitude': 149},
                'update': '2023-05-10T12:20:02+02:00', 'forecast':
                [{'insee': '78117', 'cp': 78530, 'latitude': 48.7718, 'longitude': 2.1239, 'datetime': '2023-05-10T12:00:00+0200', 'temp2m': 13, 'rh2m': 73, 'wind10m': 14, 'gust10m': 38, 'dirwind10m': 266, 'rr10': 0, 'rr1': 0, 'probarain': 60, 'weather': 10, 'probafrost': 0, 'probafog': 0, 'probawind70': 0, 'probawind100': 0, 'tsoil1': 14, 'tsoil2': 12, 'gustx': 38, 'iso0': -99},
                {'insee': '78117', 'cp': 78530, 'latitude': 48.7718, 'longitude': 2.1239, 'datetime': '2023-05-10T15:00:00+0200', 'temp2m': 15, 'rh2m': 63, 'wind10m': 14, 'gust10m': 38, 'dirwind10m': 264, 'rr10': 0.8, 'rr1': 1.6, 'probarain': 80, 'weather': 44, 'probafrost': 0, 'probafog': 0, 'probawind70': 0, 'probawind100': 0, 'tsoil1': 17, 'tsoil2': 13, 'gustx': 47, 'iso0': -99},
                {'insee': '78117', 'cp': 78530, 'latitude': 48.7718, 'longitude': 2.1239, 'datetime': '2023-05-10T18:00:00+0200', 'temp2m': 15, 'rh2m': 69, 'wind10m': 17, 'gust10m': 47, 'dirwind10m': 292, 'rr10': 4, 'rr1': 9, 'probarain': 90, 'weather': 212, 'probafrost': 0, 'probafog': 0, 'probawind70': 0, 'probawind100': 0, 'tsoil1': 17, 'tsoil2': 13, 'gustx': 57, 'iso0': -99},
                {'insee': '78117', 'cp': 78530, 'latitude': 48.7718, 'longitude': 2.1239, 'datetime': '2023-05-10T21:00:00+0200', 'temp2m': 13, 'rh2m': 79, 'wind10m': 11, 'gust10m': 31, 'dirwind10m': 286, 'rr10': 1.7000000000000002, 'rr1': 3.5, 'probarain': 70, 'weather': 40, 'probafrost': 0, 'probafog': 0, 'probawind70': 0, 'probawind100': 0, 'tsoil1': 15, 'tsoil2': 13, 'gustx': 34, 'iso0': -99}]}

        return render_template("weather.html", city=code_ville, data=data)
    return render_template("weather.html")

@app.route("/cities")
def donner_villes():
    return send_file(os.path.join(os.getcwd(), "data/donnees_villes_france.json"), mimetype="application/json")

