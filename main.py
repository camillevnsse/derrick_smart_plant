import json, requests
from flask import Flask, render_template, request
from notification import NotificationApi

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/settings")
def settings():
    return render_template("settings.html")


@app.route("/statistics")
def statistics():
    data = [
        ("1", 63),
        ("2", 47),
        ("3", 95),
        ("4", 48),
        ("5", 39)
    ]

    labels = [row[0] for row in data]
    values = [row[1] for row in data]
    return render_template("statistics.html", labels=labels, values=values)


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
