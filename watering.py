# envoie une notification au téléphone portable via Pushbullet lorsque la plante est arrosée

import json

from pushbullet import Pushbullet


class WateringApi:
    def water():
        pb = Pushbullet("o.gFohQYe13yA2DzNP2J199J7qZQF2R34S")
        push = pb.push_note("Derrick", "Arrosage de votre plante en cours...")
