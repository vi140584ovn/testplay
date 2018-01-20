import bottle
import bottle_mysql

app = bottle.Bottle()
# dbhost is optional, default is localhost
plugin = bottle_mysql.Plugin(dbhost='172.18.1.13', dbuser='user', dbpass='pass', dbname='test')
app.install(plugin)

@app.route('/show/<name>/<pass1>')
def show(name, pass1, db):
    db.execute('SELECT * from users where name=%s and pass=password(%s)', (name,pass1,))
    row = db.fetchone()
    if row:
        return row
    return "error"

app.run(host='', port=8080)
