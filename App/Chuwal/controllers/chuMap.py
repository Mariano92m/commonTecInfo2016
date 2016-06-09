# -*- coding: utf-8 -*-
from gluon.serializers import loads_json

def index():
    return dict()

@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)

def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()

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
