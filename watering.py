# fichier provisoire en attendant d'avoir mis en place le dispositif d'arrosage automatique

import json

from pushbullet import Pushbullet


class WateringApi:
    def water():
        pb = Pushbullet("o.gFohQYe13yA2DzNP2J199J7qZQF2R34S")
        push = pb.push_note("Derrick", "Arrosage de votre plante en cours...")
