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
    mc=mulChoice()

    return dict(sculp=sculp, mc=mc)

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

def correcto(d):
    s=setIDFromURL()
    if (d==s.title):
        return True
    elif (d==s.author):
        return True
    elif (d==s.material):
        return True
    elif (d==s.country):
        return True
    elif (d==s.yearCreate):
        return True
    else:
        return False

#def correcto():
#    if session.op1 == (db(db.sculpture.id == setIDFromURL()).select())[0].

#///////////////////////////////////////////////////////////////////////////////////////////////#
#Cambia el color del marcador dependiendo si esta cazada o no
def setMarkerColor():
    hunt = db(db.sculpturEstado.nickname == session.nickname).select()      
    for i in hunt:
        if i.sculpture_id==place.sculpture_id:
            z=1
    if(z==1):
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
        x=setMarkerColor()
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
            'cazada' : row.cazada,
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
#Reorganiza la lista de opciones que se van a mostrar               #Done
def randOrd(eList):
    random.shuffle(eList)
    return (eList)

#///////////////////////////////////////////////////////////////////////////////////////////////#
#Elige una opcion de manera aleatoria                               #Done

def randQ(arg):
    sculp=setIDFromURL()

    switcher = {
        0: mulChoT(sculp.title), #Name
        1: mulChoM(sculp.material),#Material
        2: mulChoY(sculp.yearCreate),#Year
        3: mulChoC(sculp.country),#Country
        4: mulChoA(sculp.author) #Author
    }
    func= switcher.get(arg, "Error")
    return func

#Random argument
def arg():
    arg=random.randrange(0,5)
    return arg

#///////////////////////////////////////////////////////////////////////////////////////////////#
#Setea la id de la escultura                                        #Done
def setIDFromURL():
    idNum= getId(URL(args=request.args, vars=request.get_vars, host=True))
    sculp= db.sculpture(idNum)
    return sculp

#///////////////////////////////////////////////////////////////////////////////////////////////#
#Pregunta si existe un elemento en la lista                         #Done
def existe(lista, elemento):
    for i in lista:
        if(i==elemento):
            return True
    return False

#///////////////////////////////////////////////////////////////////////////////////////////////#
#Crea el multiple choice y lo reordena                              #Done
def mulChoice():
    l=randQ(arg())
    a=randOrd(l)
    return (a)

def none(dato):
    if(dato == '-'):
        n= "Ninguna de las anteriores"
    else:
        n=dato
    return n

#///////////////////////////////////////////////////////////////////////////////////////////////#
#Chanchada
#///////////////////////////////////////////////////////////////////////////////////////////////#

#Multiple choice de material
def mulChoM(esc):
    lis=[none(esc)]
    sc = len(db(db.sculpture.id >0 ).select())
    scu = db(db.sculpture.id >random.randrange(sc-10)).select()

    for i in scu:
        n= i.material
        if(len(lis) < 4):
            n=none(n)
            if((n != esc) and (existe(lis,n)==False)):
                lis.append(n)
    return (lis)

#Multiple choice de material
def mulChoT(esc):
    lis=[none(esc)]
    sc = len(db(db.sculpture.id >0 ).select())
    scu = db(db.sculpture.id >random.randrange(sc-10)).select()

    for i in scu:
        n= i.title
        if(len(lis) < 4):
            n=none(n)
            if((n != esc) and (existe(lis,n)==False)):
                lis.append(n)
    return (lis)

#Multiple choice de material
def mulChoC(esc):
    lis=[none(esc)]
    sc = len(db(db.sculpture.id >0 ).select())
    scu = db(db.sculpture.id >random.randrange(sc-10)).select()

    for i in scu:
        n= i.country
        if(len(lis) < 4):
            n=none(n)
            if((n != esc) and (existe(lis,n)==False)):
                lis.append(n)
    return (lis)

#Multiple choice de material
def mulChoY(esc):
    lis=[none(esc)]
    sc = len(db(db.sculpture.id >0 ).select())
    scu = db(db.sculpture.id >random.randrange(sc-10) ).select()

    for i in scu:
        n= i.yearCreate
        if(len(lis) < 4):
            n=none(n)
            if((n != esc) and (existe(lis,n)==False)):
                lis.append(n)
    return (lis)

#Multiple choice de material
def mulChoA(esc):
    lis=[none(esc)]
    sc = len(db(db.sculpture.id >0 ).select())
    scu = db(db.sculpture.id >random.randrange(sc-10) ).select()

    for i in scu:
        n= i.author
        if(len(lis) < 4):
            n=none(n)
            if((n != esc) and (existe(lis,n)==False)):
                lis.append(n)
    return (lis)