import json
from flask import Flask, render_template, request
from notification import NotificationApi
import db_test

app = Flask(__name__)


@app.route("/")
def home():
    dt = db_test.result
    hum = dt[0][0]
    temp = dt[0][1]
    return render_template("home.html", hum=hum, temp=temp)


@app.route("/settings")
def settings():
    return render_template("settings.html")


@app.route("/statistics")
def statistics():
    dt = db_test.result
    labels = [i for i in range(len(dt))]
    hum_values = [j[0] for j in dt]
    temp_values = [k[1] for k in dt]
    water_lvl_values = [l[2] for l in dt]
    healthy_values = [m[3] for m in dt]

    return render_template("statistics.html", labels=labels, hum_values=hum_values, temp_values=temp_values, water_lvl_values=water_lvl_values, healthy_values=healthy_values)


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


@app.route("/notification")
def test_notif():
    NotificationApi.test_notification()
    return json.dumps({"status": 200, "notification_status": "correct"})


if __name__ == "__main__":
    app.run(debug=True)
