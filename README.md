# Projet Derrick

### table des matières
- [introduction](#introduction)
- [principe](#principe)
- [lancement du projet](#lancement-du-projet)

### INTRODUCTION
facilitation de l'entretien des plantes domestiques 

### PRINCIPE
- visualisation en temps réel de données telles que la température ambiante ou l'humidité du sol.
- l'application permet d'interagir avec la plante en automatisant l'arrosage à une fréquence donnée ou bien en l'arrosant manuellement à distance
- il est également possible de converser avec un chatbot pour obtenir des informations sur l'entretien de plantes

### LANCEMENT DE LA PARTIE SERVEUR DU PROJET EN VERSION TEST
- télécharger les fichiers de la branche "main"
- le fichier (requirements.txt) contient tous les modules nécessaires au lancement du projet. Vous pouvez les installer comme suit :
  - sous windows, ouvrir l'invite de commandes et naviguer vers le dossier du projet à l'aide de la commande "cd [nom du dossier]" puis entrer la commande "pip install -r requirements.txt"
- depuis le dossier source, lancer en parallèle les fichiers [run.py](run.py) et [test_client.py](test_client.py)
- dans le navigateur, entrer l'adresse suivante : "http://127.0.0.1:5000". Vous avez maintenant accès au serveur web du projet, qui tourne sur le port 5000.
  - dans cette version de test, vous avez accès uniquement à la version test du projet, avec des données générées aléatoirement.

### SECTIONS DU SERVEUR WEB
1) Accueil : affiche les données de température, d'humidité du sol et de niveau d'eau dans le réservoir en temps réel.
2) Paramètres : permet de modifier la fréquence d'envoi des données des capteurs ainsi que la fréquence d'arrosage automatique. Permet également d'arroser manuellement la plante.
3) Statistiques : visualise et met à jour en temps réel les données reçues par les capteurs dans des graphiques différents. Seulement les 10 dernières données sont affichées à l'écran pour plus de lisibilité.
4) Météo : Permet d'accéder à diverses informations météorologiques pour un lieu donné.
5) Chatbot : Permet d'interagir avec un chatbot et notamment d'obtenir des renseignements sur l'entretien de certaines plantes comme le basilic ou le cactus.

### PROJET COMPLET : MONTAGE PHYSIQUE

il est impossible de lancer la version complète du projet (branche "montage") sans avoir le montage physique. Celui-ci permet de fournir au serveur web les données affichées à l'écran (qui ne sont pas aléatoires, contrairement à la version test), et permet d'arroser la plante à une certaine fréquence ou sur un clic de l'utilisateur.
