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

def getUrlImagen(id):
    file_id = 1
    import cStringIO 
    import contenttype as c
    s=cStringIO.StringIO() 
    (filename,file) = db.sculpture.fileImage.retrieve(db.sculpture[file_id].fileImage)
    return s.write(file.read()) 
    

#Controlador para el mapa
def getMarkers():
    places = []
    rows = db(db.place.id >0 ).select()

    for row in rows:
        if(row.cazada=='S'):
            x="\Chuwal\static\images\PinVerde.png"
        else:
            x="\Chuwal\static\images\PinRojo.png"
        
        try:
            imagen= getUrlImagen(1)
        except:
            imagen ="https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Run.svg/744px-Run.svg.png "
        
        html = '<img src="'+ imagen +'">'
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
