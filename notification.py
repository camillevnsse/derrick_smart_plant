import json

from pushbullet import Pushbullet


class NotificationApi:
    def test_notification():
        pb = Pushbullet("o.gFohQYe13yA2DzNP2J199J7qZQF2R34S")
        push = pb.push_note("Derrick", "Bonjour ! je suis Derrick, votre assistant !")
