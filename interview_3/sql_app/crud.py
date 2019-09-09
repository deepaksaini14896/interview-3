from sqlalchemy.orm import Session

from . import models
from .database import engine

import json
import os


def get_place(db: Session, lat: float, lng: float):
    return db.query(models.GPS).filter(models.GPS.latitude == lat, models.GPS.longitude == lng).first()


def create_table():
    db = engine.connect()
    db.execute("CREATE TABLE IF NOT EXISTS cities(id integer primary key,city varchar, area varchar, state varchar, latitude numeric(17,15), longitude numeric(17,15))")
    if db.execute("SELECT * FROM cities").first():
        print('Database retrive')
    else:
        a = os.getcwd()
        b = os.path.join(a,"map.geojson")
        c = open(b, "r")
        d = c.read()
        json_raw = json.loads(d)
        id = 1
        for i in json_raw['features']:
            city = i['properties']['name']
            area = i['properties']['type']
            state = i['properties']['parent']
            coords = i['geometry']['coordinates'][0]
            id = add_to_table(db, id, city, area, state, coords)
        print('Database succesfully added')
        c.close()
    db.close()


def add_to_table(db, id, city, area, state, coords):
    latitudes = []
    longitudes = []
    for coord in coords:
        latitudes.append(coord[0])
    for coord in coords:
        longitudes.append(coord[1])
    for latitude, longitude in zip(latitudes,longitudes):
        insert_to_table(db, id ,city, area, state, latitude, longitude)
        id += 1
    return id

def insert_to_table(db, id, city, area, state, latitude, longitude):
    db.execute("INSERT INTO cities VALUES (%s,%s,%s,%s,%s,%s)",(id, city, area, state, latitude, longitude))