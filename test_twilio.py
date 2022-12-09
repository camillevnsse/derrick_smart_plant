# bon au final c'est pas avec twilio mais pushbullet mais c'est pas grave
from pushbullet import Pushbullet

pb = Pushbullet("o.gFohQYe13yA2DzNP2J199J7qZQF2R34S")
push = pb.push_note("Derrick", "Bonjour ! je suis Derrick, votre assistant !")
print('ok')
