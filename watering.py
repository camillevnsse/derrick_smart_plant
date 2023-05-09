import requests
from pushbullet import Pushbullet


class WateringApi:
    def water():
        print('ok')
        try:
            requests.post("http://192.168.0.39/water")
        except Exception as err:
            print(err)

        pb = Pushbullet("o.gFohQYe13yA2DzNP2J199J7qZQF2R34S")
        push = pb.push_note("Derrick", "Arrosage de votre plante en cours...")

        print('plante arrosée !')
