from bottle import route, run, template

@route('/')
def index():
#    return template('<b>Hello world</b>!',name=name)
     return template('temp.tpl')


#from bottle import route, run, template

#@route('/hello/<name>')
#def index(name):
#    return template('<b>Hello {{name}}</b>!', name=name)

run(host='', port=8080)
