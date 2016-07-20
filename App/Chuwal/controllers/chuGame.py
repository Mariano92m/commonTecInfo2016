from gluon.serializers import loads_json
import random
#HTML
#///////////////////////////////////////////////////////////////////////////////////////////////#
def chuMap():
    if session.nickname!='':
        return dict()
    else:
        redirect(URL('chuInterface','chuRegister'))

#///////////////////////////////////////////////////////////////////////////////////////////////#
def chuSculptInfo():
    if session.nickname!='':
        idNum= getId(URL(args=request.args, vars=request.get_vars, host=True))
        sculp= db.sculpture(idNum)
        return dict(sculp=sculp)
    else:
        redirect(URL('chuInterface','chuRegister'))
    

#///////////////////////////////////////////////////////////////////////////////////////////////#
#Controladores para la Lista
def chuList():
    if session.nickname!='':
        #en rows almaceno todos los registros de sculpture cuya ID sea mayor a cero
        places=db().select(db.place.ALL,orderby=db.place.id)

        #Usuario actual
        userId=db(db.cazador.nickname==session.nickname).select(db.cazador.id)
        uEst=db(db.sculpturEstado.cazador_id == userId[0].id).select()

        return dict(places=places, uEst=uEst)
    else:
        redirect(URL('chuInterface','chuRegister'))

#///////////////////////////////////////////////////////////////////////////////////////////////#
def chuHunt():
    if session.nickname!='':
        idNum= getId(URL(args=request.args, vars=request.get_vars, host=True))
        sculp= db.sculpture(idNum)
        mc,p=mulChoice()
        return dict(sculp=sculp, mc=mc, p=p)
    else:
        redirect(URL('chuInterface','chuRegister'))

#///////////////////////////////////////////////////////////////////////////////////////////////#
def chuHuntCorrecta():
    idS=URL(args=request.args)
    sculp=db.sculpture(idS)
    return dict(sculp=sculp)
#///////////////////////////////////////////////////////////////////////////////////////////////#
def chuHuntIncorrecta():
    idS=URL(args=request.args)
    sculp=db.sculpture(idS)
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
def getId(url):
    cont=0
    cn=0
    for i in url:
        if (i=='='):
            cn=cont
        cont=cont+1
    numId=url[cn+1: len(url)]
    return numId

def divide(d):
    argu1 =d.split('/')[4]
    argu2 =d.split('/')[5]
    return argu1, argu2

def respuesta():
    dato=URL(args=request.args)
    s,d=divide(dato)
    r=correcto(s,d)

    if r == True:
        userId=db(db.cazador.nickname==session.nickname).select(db.cazador.id)
        db.sculpturEstado.insert(cazador_id=userId[0].id,pId=s)
        redirect(URL('chuGame','chuHuntCorrecta',args=s))
    else:
        redirect(URL('chuGame','chuHuntIncorrecta',args=s))
    

def correcto(s,d):
    rows = db(db.sculpture.id == s ).select()
    f=False
    for i in rows:
        if (d==i.title):
            f=True
        elif (d==i.author):
            f=True
        elif (d==i.material):
            f=True
        elif (d==i.country):
            f=True
        elif (d==i.yearCreate):
            f=True

    return f

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
            but='<a href="chuHunt.html?args='+str(sc)+'" class="btn">Cazar</a>'
    else:
        but='<a href="#" class="btn">Error</a>';
    return but

#///////////////////////////////////////////////////////////////////////////////////////////////#
#Marcadores
def getMarkers():
    places = []

    #Usuario actual
    userId=db(db.cazador.nickname==session.nickname).select(db.cazador.id)
    uEst=db(db.sculpturEstado.cazador_id == userId[0].id).select()
    

    #Places
    rows = db(db.place.id >0 ).select()

    for row in rows:
        ima=row.sculpture_id.fileImageNHURL
        idS=row.sculpture_id
        lat=row.lat
        lng=row.lng
        name=row.name

        for i in uEst:
            #Compara la id de palce con la id que deberia almacenarse en pId
            if str(row.id) == str(i.pId):
                condition='S'
                pla=mark(condition, ima, idS, lat, lng, name)
                places.append(pla)

            #Si no son iguales muestra no cazada
            elif str(row.id) != str(i.pId):
                condition='N'
                pla=mark(condition, ima, idS, lat, lng, name)
                places.append(pla)

    return response.json(places)

def mark(condition, ima, idS, lat, lng, name):
    #Color del marcador
    x=setMarkerColor(condition)
    #Imagen de la escultura
    imagen= showIMG(condition, ima)
    #Boton
    but= showBut(condition, ima, idS)
    #Codigo html va en este sector
    html =  (
            '<div class="container" style="width: 200px;">'
                '<center>''<img src=' + imagen + ' style="width: 100%;"/>''</center>'
                '<center>''<button>'+ but +'</button>''</center>'
            '</div>'
            )
    #Setea la informacion de los marcadores
    place = {
        'lat' : lat,
        'lng' : lng,
        'name' : name,
        'cazada' : condition,
        'icon': x,
        'infoWindow' : {
            'content' : html,
            'maxWidth' : 200
        },
        'onClick':{}
    }
    return place

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
    sw = {
        0:"¿Cual es el nombre de a escultura?",
        1:"¿De que material esta hecha la escultura?",
        2:"¿En que año fue creada?",
        3:"¿De que pais es/son el/los autor/es de la escultura?",
        4:"¿Como se llama el/los autor/es de la escultura?"
    }
    func= switcher.get(arg, "Error")
    p= sw.get(arg,"Error")
    return func, p

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
    m,p=randQ(arg())
    m=randOrd(m)
    return (m,p)

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