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


@app.route("/statistiques")
def statistiques():
    return render_template("statistiques.html")


from notification import NotificationApi


@app.route("/notification")
def test_notif():
    NotificationApi.test_notification()
    return json.dumps({"status": 200, "notification_status": "correct"})


if __name__ == "__main__":
    app.run(debug=True)
