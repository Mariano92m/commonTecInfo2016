def chuHome():
	if session.nickname!='':
		return dict()
	else:
		redirect(URL('chuInterface','chuRegister'))

def chuProfile():
	if session.nickname!='':
		return dict()
	else:
		redirect(URL('chuInterface','chuRegister'))

def chuUs():
	return dict()

def chu404():
	return dict()

def chuHelp():
	return dict()

def chuWelcome():
	return dict()

def chuRelated():
	return dict()

def chuRegister():
	return dict()