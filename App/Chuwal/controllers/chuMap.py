# -*- coding: utf-8 -*-
from gluon.serializers import loads_json

def index():
    return dict()

#Controlador para el mapa
def getMarkers():
    places = []
    rows = db(db.place.id >0 ).select()

    for row in rows:
        if(row.cazada=='S'):
            x="\Chuwal\static\images\PinVerde.png"
        else:
            x="\Chuwal\static\images\PinRojo.png"
        place = {
            'lat' : row.lat,
            'lng' : row.lng,
            'name' : row.name,
            'cazada':row.cazada,
            'icon': x,
            'infoWindow' : {'content': "<p>" +row.descr + "</p>"}
        }
        places.append(place)
    return response.json(places)
