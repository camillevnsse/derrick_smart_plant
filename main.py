import json

from flask import Flask, render_template
from pushbullet import Pushbullet

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


from notification import NotificationApi


@app.route("/notification")
def test_notif():
    NotificationApi.test_notification()
    return json.dumps({"status": 200, "notification_status": "correct"})


if __name__ == "__main__":
    app.run(debug=True)
