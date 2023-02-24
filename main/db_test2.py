from flask_sqlalchemy import SQLAlchemy
from random import random
from main import db


max_data_amount = 10


#création des tables pour chacune des grandeurs mesurées
class Hum(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    values = db.Column(db.Float)
    dates = db.Column(db.String)

    def __repr__(self):
        return f"Hum('{self.values}', '{self.dates}')"

class Temp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    values = db.Column(db.Float)
    dates = db.Column(db.String)

    def __repr__(self):
        return f"Temp('{self.values}', '{self.dates}')"

class Wat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    values = db.Column(db.Float)
    dates = db.Column(db.String)

    def __repr__(self):
        return f"Wat('{self.values}', '{self.dates}')"

db.create_all()


#fonctions pour ajouter/supprimer/obtenir des données dans la db

def add_data(data_type, value_add, date_add):

    if data_type == "humidity":
        for i in range(max_data_amount-1):
            Hum.query.get_or_404(i+1).values = Hum.query.get_or_404(i+2).values
            Hum.query.get_or_404(i+1).dates = Hum.query.get_or_404(i+2).dates
        add_hum = Hum.query.get_or_404(10)
        add_hum.values = value_add
        add_hum.dates = date_add

    if data_type == "temperature":
        for i in range(max_data_amount-1):
            Temp.query.get_or_404(i+1).values = Temp.query.get_or_404(i+2).values
            Temp.query.get_or_404(i+1).dates = Temp.query.get_or_404(i+2).dates
        add_temp = Temp.query.get_or_404(10)
        add_temp.values = value_add
        add_temp.dates = date_add
    
    if data_type == "water_lvl":
        for i in range(max_data_amount-1):
            Wat.query.get_or_404(i+1).values = Wat.query.get_or_404(i+2).values
            Wat.query.get_or_404(i+1).dates = Wat.query.get_or_404(i+2).dates
        add_wat = Wat.query.get_or_404(10)
        add_wat.values = value_add
        add_wat.dates = date_add
        
    db.session.commit()


def get_last_data(data_type, amount):

    if amount > max_data_amount:
        print("index list out of range ! gngngng :p")

    else:
        if data_type == "humidity":
            return [Hum.query.all()[-i].values for i in range(1, amount+1)]

        if data_type == "temperature":
            return [Temp.query.all()[-i].values for i in range(1, amount+1)]

        if data_type == "water_lvl":
            return [Wat.query.all()[-i].values for i in range(1, amount+1)]


def reset_db():

    db.session.close()
    db.drop_all()
    db.create_all()

    for i in range(max_data_amount):
        hum_add = Hum(values=0, dates="")
        temp_add = Temp(values=0, dates="")
        wat_add = Wat(values=0, dates="")
        db.session.add(hum_add)
        db.session.add(temp_add)
        db.session.add(wat_add)
    
    db.session.commit()

'''
hum_values = Hum.query.all()
temp_values = Temp.query.all()
wat_values = Wat.query.all()
print(hum_values)
print(temp_values)
print(wat_values)
'''