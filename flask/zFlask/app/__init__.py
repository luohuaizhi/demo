from flask import Flask
from flask import render_template, g
import sqlite3

app = Flask(__name__)
DATABASE = '/path/to/database.db'


def connect_db():
    return sqlite3.connect(DATABASE)


def d_b():
    _db = getattr(g, 'db', None)
    if _db is None:
        _db = g.db = connect_db()
    return _db


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', error=str(error)), 404


@app.errorhandler(500)
def server_error(error):
    return render_template('500.html', error=str(error)), 500


@app.before_request
def before_request():
    g.db = connect_db()


@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()
