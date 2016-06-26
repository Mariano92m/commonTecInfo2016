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



#Cambia el color del marcador dependiendo si esta cazada o no
def setMarkerColor(cazada):
    if(cazada=='S'):
        return "\Chuwal\static\images\PinVerde.png"
    else:
        return "\Chuwal\static\images\PinRojo.png"

#Muestra una imagen dependiendo si esta cazada o no
def showIMG(condition, img, imgNH):
    if(condition=='S'):
        imagen= '"' + img + '"';
    elif(condition=='N' and imgNH != "none"):
        imagen= '"' + imgNH + '"';
    else:
        imagen ="https://media.giphy.com/media/pSpmpxFxFwDpC/giphy.gif"
    return imagen

#Muestra un boton dependiendo si esta cazada o no
def showBut(condition, imgNH):
    if(condition=='S'):
        but='<a href="#" class="btn">Ver info</a>';
    elif(condition=='N' and imgNH != "none"):
        but='<a href="#" class="btn">Cazar</a>';
    else:
        but='<a href="#" class="btn">Error</a>';
    return but

#Controlador para el mapa
def getMarkers():
    places = []
    rows = db(db.place.id >0 ).select()

    for row in rows:
        #Color del marcador
        x=setMarkerColor(row.cazada)
        
        #Imagen de la escultura
        imagen= showIMG(row.cazada, row.sculpture_id.fileImageURL, row.sculpture_id.fileImageNHURL)
        
        #Boton
        but= showBut(row.cazada, row.sculpture_id.fileImageNHURL)
        
        #Codigo html va en este sector
        html =  (
                '<div class="container" style="width: 200px;">'
                    '<center>''<img src=' + imagen + ' style="width: 100%;"/>''</center>'
                    '<center>''<button id="but1">'+ but +'</button>''</center>'
                '</div>'
                ) 
        
        #Setea la informacion de los marcadores
        place = {
            'lat' : row.lat,
            'lng' : row.lng,
            'name' : row.name,
            'cazada':row.cazada,
            'icon': x,
            'infoWindow' : {
                'content' : html,
                'maxWidth' : 200
            },
            'onClick':{}
        }

        #Agrega un marcador a la lista de marcadores
        places.append(place)
    return response.json(places)