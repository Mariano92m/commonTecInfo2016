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

def getMarkers():
    sculptures = []
    rows = db(db.sculptures.id >0 ).select()

    for row in rows:
        
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
        
        #Setea la informacion de cada fila
        sculpture = {
            'name' : row.name,
            'cazada':row.cazada,
            'dirección': 'direccion',
            'image': 'imagen',
            'onClick':{}
        }

        #Agrega un marcador a la lista de marcadores
        places.append(place)
    return response.json(places)
