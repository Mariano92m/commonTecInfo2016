from gluon.serializers import loads_json
#HTML
def chuMap():
	return dict()

def chuSculptInfo(esc):
    #Info Importante
    tit=esc.sculpture_id.title
    aut=esc.sculpture_id.author
    cou=esc.sculpture_id.country
    mat=esc.sculpture_id.material
    yea=esc.sculpture_id.yearCreate

    #Info Extra
    adr=esc.sculpture_id
    awa=esc.sculpture_id

    #Imagen Cuadrada
    img=esc.sculpture_id.fileImageURL
    return dict(tit=tit, aut=aut, cou=cou, mat=mat, yea=yea, adr=adr, awa=awa)

def chuList(esc):
	return dict()

def chuHunt(esc):
    #Info Importante
    tit=esc.sculpture_id.title
    aut=esc.sculpture_id.author
    cou=esc.sculpture_id.country
    mat=esc.sculpture_id.material
    yea=esc.sculpture_id.yearCreate

    #Imagen Cuadrada
    img=esc.sculpture_id.fileImageNHURL
	return dict()


#Controladores para el Mapa
@cache.action()
def download():
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
def showIMG(condition, imgC):
    if(imgC!="none"):
        if(condition=='S'):
            ima= '"' + imgC + '"';
        else:
            ima= '"' + imgC + '"';
    else:
        ima ="https://media.giphy.com/media/pSpmpxFxFwDpC/giphy.gif"
    return ima

#Muestra un boton dependiendo si esta cazada o no
def showBut(condition, imgC):
    if(imgC!="none"):
        if(condition=='S'):
            but='<a href="#" class="btn">Ver info</a>';
        else:
            but='<a href="#" class="btn">Cazar</a>';
    else:
        but='<a href="#" class="btn">Error</a>';
    return but

#Marcadores
def getMarkers():
    places = []
    rows = db(db.place.id >0 ).select()
    for row in rows:

        #Color del marcador
        x=setMarkerColor(row.cazada)
        #Imagen de la escultura
        imagen= showIMG(row.cazada, row.sculpture_id.fileImageNHURL)
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

#Controladores para la Lista

#Controladores para Cazar
def randQ():

def correct():

def nameSculpt():

def mcMaterial():

def mcYear():

def mcCountry():

def mcAuthor():