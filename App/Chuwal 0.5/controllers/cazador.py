def login():
	datos = request.post_vars
	row = db(db.cazador.nickname == datos.nick, db.cazador.password==datos.password).select()
	if len(row)==0:
		response.view = "chuInterface/chuWelcome.html"
		return dict(msj="Usuario no existe")
	else:
		response.view = "chuInterface/chuHome.html"
		session.id=row[0].id
		session.nickname = datos.nick
		return dict()


def cerrarSession():
	session.nickname = ""
	session.id=None
	response.view = "chuInterface/chuRegister.html"
	return dict()

def registro():
	datos = request.post_vars
	row = db(db.cazador.nickname == datos.nick, db.cazador.password==datos.password).select()
	if len(row)!=0:
		response.view = "chuInterface/chuRegister.html"
		return dict(error="usuario ya esta registrado")
	else:
		response.view = "chuInterface/chuHome.html"
		db.cazador.insert(nickname=datos.nick,password=datos.password,email=datos.email)
		session.nickname = datos.nick
		row = db(db.cazador.nickname == datos.nick, db.cazador.password==datos.password).select()
		session.id = row[0].id
		return dict(error="Registro Completo")