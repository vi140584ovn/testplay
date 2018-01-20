import MySQLdb

def conn():
        db = MySQLdb.connect('172.18.1.13','user','pass','test')
        cur = db.cursor(MySQLdb.cursors.DictCursor)
        return [db,cur]

def query(user, passwd):
        db,cur = conn()
        cur.execute('SELECT * from users where name=%s and pass=password(%s)', (user,passwd,))
        row = cur.fetchone()
        db.close()
        return row

def queryall():
        db,cur = conn()
        cur.execute('SELECT * from users')
        row=cur.fetchall()
        db.close()
        return row

def queryinsert(user,passwd,role):
        db,cur = conn()
        cur.execute('insert into users(name,pass,role) value(%s, password(%s), %s)', (user,passwd,int(role)))
        db.commit()
        db.close()

def queryupdatepass(user,passwd):
        db,cur = conn()
        cur.execute('update users set pass=password(%s) where name=%s', (passwd,user))
        db.commit()
        db.close()

def queryupdaterole(user,role):
        db,cur = conn()
        cur.execute('update users set role=%s where name=%s', (int(role),user))
        db.commit()
        db.close()

def querydelete(user):
        print user
        db,cur = conn()
        cur.execute('delete from users where name=%s', (user))
        db.commit()
	db.close()

def queryone(user):
        db,cur = conn()
        cur.execute('SELECT * from users where name=%s', (user))
        row = cur.fetchall()
        db.close()
        return row

def queryonetwo():
        db,cur = conn()
        cur.execute('SELECT * from users where role = 1 or role = 2')
        row = cur.fetchall()
        db.close()
        return row

