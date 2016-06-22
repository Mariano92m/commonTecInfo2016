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

def somefunction():
    pic = db(db.sculpture).select().first().picture   #select first picture
    return dict(pic=pic)

def setMarkerColor(cazada):
    if(cazada=='S'):
        return "\Chuwal\static\images\PinVerde.png"
    else:
        return "\Chuwal\static\images\PinRojo.png"

def showIMG(condition, img, imgNH):
    if(condition=='S'):
        imagen= '"' + img + '"'
    elif(condition=='N' and imgNH != "none"):
        imagen= '"' + imgNH + '"'
    else:
        imagen ="http://cdn.quotesgram.com/small/44/82/67139225-46070194.jpg"
    return imagen

#Controlador para el mapa
def getMarkers():
    places = []
    rows = db(db.place.id >0 ).select()

    for row in rows:
        x=setMarkerColor(row.cazada)

        imagen= showIMG(row.cazada, row.sculpture_id.fileImageURL, row.sculpture_id.fileImageNHURL)
                   
        html = '<p>' '<img src=' + imagen + ' width="200px" />' '</p>'
        place = {
            'lat' : row.lat,
            'lng' : row.lng,
            'name' : row.name,
            'cazada':row.cazada,
            'icon': x,
            'infoWindow' : {'content' : html },
            'onClick':{}
        }
        places.append(place)
    return response.json(places)
