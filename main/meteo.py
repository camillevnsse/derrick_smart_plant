from flask import render_template, request, send_file
from main import app, socketio
import requests as req
import json
import dotenv, os

dotenv.load_dotenv()
TOKEN_API_METEO=os.getenv("TOKEN_API_METEO")

def get_weather_dat(cityname):
    Resp = req.get(f'https://api.meteo-concept.com/api/forecast/nextHours?token={TOKEN_API_METEO}&insee={num_insee}')
    Data[num_insee] = json.loads(Resp.text)
    return Data

@app.route("/weather", methods=["GET"])
def get_weather():
    cityname = request.args.get("city", False)
    if cityname:
        data = get_weather_dat(cityname)
        
        
        

        # r = requests.get(url_path)
        # data = r.json()
        data = {'coord': {'lon': -0.1257, 'lat': 51.5085},
                'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}],
                'base': 'stations',
                'main': {'temp': 14.29, 'feels_like': 13.16, 'temp_min': 12.25, 'temp_max': 15.86, 'pressure': 1015,
                         'humidity': 53}, 'visibility': 10000, 'wind': {'speed': 4.63, 'deg': 280},
                'clouds': {'all': 100}, 'dt': 1664128421,
                'sys': {'type': 2, 'id': 2075535, 'country': 'GB', 'sunrise': 1664085064, 'sunset': 1664128404},
                'timezone': 3600, 'id': 2643743, 'name': cityid, 'cod': 200}

        return render_template("weather.html", city=cityid, data=data)

    return render_template("weather.html")

@app.route("/cities")
def donner_villes():
    return send_file(os.path.join(os.getcwd(), "data/donnees_villes_france.json"), mimetype="application/json")