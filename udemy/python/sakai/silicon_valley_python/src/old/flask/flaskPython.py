import sqlite3

from flask import Flask
from flask import g
from flask import render_template
from flask import request
from flask import Response


app = Flask(__name__)


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('test_sqliteFlask.db')
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()



@app.route('/')
def hello_world():
    return 'top'

@app.route('/hello')
@app.route('/hello/<username>')
def hello_world2(username=None):
    # return 'hello world %s' % (username)
    return render_template('flask.html', username=username)

@app.route('/post', methods=['POST', 'PUT', 'DELETE'])
def show_post():
    return str(request.values)


@app.route('/employee', methods=['POST', 'PUT' 'DELETE'])
@app.route('/employee/<name>', methods=['GET'])
def employee(name=None):
    db = get_db()
    curs = db.cursor()
    curs.execute(
        'CREATE TABLE IF NOT EXISTS persons( '
        'id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)'
    )
    db.commit()

    name = request.values.get('name', name)
    if request.method == 'GET':
        curs.execute('SELECT * FROM persons WHERE name = "%s"' % (name))
        person = curs.fetchone()
        if not person:
            return 'No', 404
        user_id, name = pserson
        return '%s %s' % (user_id, name), 200


    if request.method == "POST":
        curs.execute('INSERT INTO persons(name) values("%s")' % (name))
        db.commit()
        return 'created %s' % (name), 201

    if request.method == "PUT":
        new_name = request.values["new_name"]
        curs.execute('UPDATE persons set name = "%s" WHERE name = "%s" ' % (new_name, name))
        db.commit()
        return 'updated %s: %s' % (name, new_name), 200

    if request.method == 'DELETE':
        curs.execute('DELETE from persons WHERE name = "%s" ' % (name))
        db.commit()
        return 'deleted %s' % (name), 200

    curs.close()



def main():
    app.debug = True
    app.run()
    # app.run(host='127.0.0.1', port=5000)

if __name__ == '__main__':
    main()
