from gluon.serializers import loads_json
import random
#HTML
#///////////////////////////////////////////////////////////////////////////////////////////////#
def chuMap():
    return dict()

#///////////////////////////////////////////////////////////////////////////////////////////////#
def chuSculptInfo():
    idNum= getId(URL(args=request.args, vars=request.get_vars, host=True))
    sculp= db.sculpture(idNum)
    return dict(sculp=sculp)

#///////////////////////////////////////////////////////////////////////////////////////////////#
#Controladores para la Lista
def chuList():
    #en rows almaceno todos los registros de sculpture cuya ID sea mayor a cero
    places=db().select(db.place.ALL,orderby=db.place.id)
    return dict(places=places)

#///////////////////////////////////////////////////////////////////////////////////////////////#
def chuHunt():
    idNum= getId(URL(args=request.args, vars=request.get_vars, host=True))
    sculp= db.sculpture(idNum)
    return dict(sculp=sculp)

#///////////////////////////////////////////////////////////////////////////////////////////////#
#Controladores para el Mapa
@cache.action()
def download():
    return response.download(request, db)

#///////////////////////////////////////////////////////////////////////////////////////////////#
def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()

#///////////////////////////////////////////////////////////////////////////////////////////////#
def somefunction():
    pic = db(db.sculpture).select().first().picture   #select first picture
    return dict(pic=pic)

#///////////////////////////////////////////////////////////////////////////////////////////////#
def getId(url):
    cont=0
    cn=0
    for i in url:
        if (i=='='):
            cn=cont
        cont=cont+1
    numId=url[cn+1: len(url)]
    return numId

#///////////////////////////////////////////////////////////////////////////////////////////////#
#Cambia el color del marcador dependiendo si esta cazada o no
def setMarkerColor(cazada):
    if(cazada=='S'):
        return "\Chuwal\static\images\PinVerde.png"
    else:
        return "\Chuwal\static\images\PinRojo.png"

#///////////////////////////////////////////////////////////////////////////////////////////////#
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

#///////////////////////////////////////////////////////////////////////////////////////////////#
#Muestra un boton dependiendo si esta cazada o no
def showBut(condition, imgC, sc):
    if(imgC!="none"):
        if(condition=='S'):
            but='<a href="chuSculptInfo.html?args='+str(sc)+'" class="btn">Ver info</a>'
        else:
            but='<a href="chuHunt.html?args='+str(sc)+'" class="btn">Cazar</a>' #56
    else:
        but='<a href="#" class="btn">Error</a>';
    return but

#///////////////////////////////////////////////////////////////////////////////////////////////#
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
        but= showBut(row.cazada, row.sculpture_id.fileImageNHURL, row.sculpture_id)
        #Codigo html va en este sector
        html =  (
                '<div class="container" style="width: 200px;">'
                    '<center>''<img src=' + imagen + ' style="width: 100%;"/>''</center>'
                    '<center>''<button>'+ but +'</button>''</center>'
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

#///////////////////////////////////////////////////////////////////////////////////////////////#
#Controladores para Cazar
#def randQ():

def randOrd(eList):
    random.shuffle(eList)
    return eList

def existe(lista, elemento):
    for i in lista:
        if(i==elemento):
            return True
    return False

def mulCho(esc, escL):
    lis=[esc]
    eL=len(escL)
    i=0;

    while(i <= eL or len(lis) < 4):
        
        r=random.randrange(i,i+5);
        if(r<=eL and len(lis) < 4):
            i=r
            print (escL[i])

            if( (escL[i] != esc) and (existe(lis,escL[i])==False)):
                lis.append(escL[i])
        else:
            return lis
            
def mulChoice(esc,escL):
    l=mulCho(esc,escL)
    l=randOrd(l)
    return (l)

#def correct():

#def mcName():

#def mcMaterial():

#def mcYear():

#def mcCountry():

#def mcAuthor():