import bottle
from mydb import * 

def check(user, passwd):
	if query(user, passwd):
		return True
	return False 

@bottle.post('/create_user_by_ajax')
def create_user():
        name = bottle.request.forms.get("name")
        passwd = bottle.request.forms.get("passwd")
        role = bottle.request.forms.get("role")
        if name == "":
                return "username is empty"
	if passwd == "":
		 return "password is empty"
        if queryone(name):
                return "username is busy"
        else:
                queryinsert(name,passwd,role)
                return "user is created"

@bottle.post('/change_user')
def change_user():
        name = bottle.request.forms.get("name")
        passwd = bottle.request.forms.get("passwd")
        role = bottle.request.forms.get("role")
	if passwd != "":
		queryupdatepass(name,passwd)
	queryupdaterole(name,role)
	bottle.redirect('/')

@bottle.post('/delete_user')
def delete_user():
        name = bottle.request.forms.get("namedel")
        querydelete(name)
	bottle.redirect('/')

@bottle.route('/static/<filepath:path>')
def server_static(filepath):
	return bottle.static_file(filepath, root='static')

@bottle.route('/')
@bottle.auth_basic(check)
def index():
	a = bottle.request.auth
	row = query(a[0], a[1])
	if row['role'] == 0:
		return bottle.template('temp.tpl',role=row['role'],name=row['name'],all=queryall())
	if row['role'] == 1:
		return bottle.template('temp.tpl',role=row['role'],name=row['name'],all=queryonetwo())
	if row['role'] == 2:
		return bottle.template('temp.tpl',role=row['role'],name=row['name'],all=queryone(row['name']))

if __name__ == '__main__':
	print "Starting server"
	bottle.run(host='0.0.0.0', port=8080, reloader=True)
