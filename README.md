# Projet Derrick

### table des matières
- [introduction](#introduction)
- [principe](#principe)
- [lancement de la partie serveur du projet en version test](#lancement-de-la-partie-serveur-du-projet-en-version-test)
- [sections du site](#sections-du-site)
- [informations sur le montage physique](#informations-sur-le-montage-physique)
- [informations générales](#informations-generales)

### INTRODUCTION
Ce projet est né d'un problème de la vie courante : l'entretien des plantes domestiques. Il s'agit donc avec le projet Derrick d'automatiser l'entretien des plantes domestiques notamment à l'aide de différents capteurs et d'une interface web pour visualiser les données qu'ils envoient. 

### PRINCIPE
- Visualisation en temps réel de données telles que la température ambiante ou l'humidité du sol.
- L'application permet d'interagir avec la plante en automatisant l'arrosage à une fréquence donnée ou bien en l'arrosant manuellement à distance
- Il est également possible de converser avec un chatbot pour obtenir notamment des informations sur l'entretien de plantes

### LANCEMENT DE LA PARTIE SERVEUR DU PROJET EN VERSION TEST
- Télécharger les fichiers de la branche "main"
- Le fichier (requirements.txt) contient tous les modules nécessaires au lancement du projet. Vous pouvez les installer comme suit :
  - sous windows, ouvrir l'invite de commandes et naviguer vers le dossier du projet à l'aide de la commande "cd [nom du dossier]" puis entrer la commande "pip install -r requirements.txt"
- Depuis le dossier source, lancer en parallèle les fichiers [run.py](run.py) et [test_client.py](test_client.py)
- Dans le navigateur, entrer l'adresse suivante : "http://127.0.0.1:5000". Vous avez maintenant accès au serveur web du projet, qui tourne sur le port 5000.
  - Dans cette version de test, vous avez accès uniquement à la version test du projet, avec des données générées aléatoirement.

### SECTIONS DU SITE
1) Accueil : affiche les données de température, d'humidité du sol et de niveau d'eau dans le réservoir en temps réel.
2) Paramètres : permet de modifier la fréquence d'envoi des données des capteurs ainsi que la fréquence d'arrosage automatique. Permet également d'arroser manuellement la plante.
3) Statistiques : visualise et met à jour en temps réel les données reçues par les capteurs dans des graphiques différents. Seulement les 10 dernières données sont affichées à l'écran pour plus de lisibilité.
4) Météo : Permet d'accéder à diverses informations météorologiques pour un lieu donné.
5) Chatbot : Permet d'interagir avec un chatbot et notamment d'obtenir des renseignements sur l'entretien de certaines plantes comme le basilic ou le cactus.

### INFORMATIONS SUR LE MONTAGE PHYSIQUE

Il est impossible de lancer la version complète du projet (branche "montage") sans avoir le montage physique. Celui-ci permet de fournir au serveur web les données affichées à l'écran (qui ne sont pas aléatoires, contrairement à la version test), et permet d'arroser la plante à une certaine fréquence ou sur un clic de l'utilisateur. Cette branche est en cours de développement.

### INFORMATIONS GENERALES
#### langages et frameworks utilisés
- Pour le serveur web : code en Python, HTML, CSS, JavaScript avec le framework Tailwind pour la mise en forme et le framwork Flask pour créer une application web
- Pour le montage physique : programmation en MicroPython avec le firmware MicroPython

#### Hardware - montage physique
- **ESP8266 wemos d1 mini** : circuit intégré à microcontrôleur avec connexion Wi-Fi. Permet de communiquer avec les différents composants du système à distance
- **Pompe à eau submersible** : permet l'arrosage de la plante.
- **Relais** : permet d'actionner la pompe.
- **Multiplexeur** : circuit logique combinatoire conçu pour commuter l'une de plusieurs lignes d'entrée sur une seule ligne de sortie commune. Permet d'avoir plusieurs entrées analogiques pour les capteurs car il n'y a pas assez de ports analogiques sur l'ESP8266.
- **capteur d'humidité sol** : mesure l'humidité du sol pour savoir quand arroser la plante. Agit comme une résistance variable qui varie avec l'humidité du sol.
- **capteur de température** : mesure la température ambiante.
- **capteur de niveau d'eau** : mesure le niveau d'eau dans le réservoir pour savoir quand le remplir de nouveau. Fonctionne comme une résistance variable; la présence d'eau entraîne un court-circuit qui permet de la détecter.
- autres : routeur 4g, mini-pc, fils de connexion, breadboard, résistances...
