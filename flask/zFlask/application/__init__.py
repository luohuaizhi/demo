from flask import Flask
from flask import render_template, request, session, abort, g
from random import random
import hashlib
import os
from application.models import db

# mysql
# db.bind('mysql', host="localhost", user="root", passwd="123123", db="t2")
# oracle
# db.bind('oracle', 'user/password@dsn')
# postgres
# db.bind('postgres', user='', password='', host='', database='')
# sqlite
db.bind('sqlite', '../db.sqlite3', create_db=True)

app = Flask(__name__, template_folder="../templates", static_folder="../static", static_url_path='/static')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('base/404.html', error=str(error)), 404


@app.errorhandler(500)
def server_error(error):
    return render_template('base/500.html', error=str(error)), 500


@app.before_request
def before_request():
    print "start request: %s( %s )" % (request.method, request.url)


@app.teardown_request
def teardown_request(exception):
    print "end request: %s( %s )" % (request.method, request.url)
    if exception:
        print exception


# @app.before_request
# def csrf_protect():
#     if request.method == "POST":
#         token = session.pop('_csrf_token', None)
#         if not token or token != request.form.get('_csrf_token'):
#             abort(403)


# def generate_csrf_token():
#     if '_csrf_token' not in session:
#         session['_csrf_token'] = gen_csrf()
#     return session['_csrf_token']
#
#
# def gen_csrf():
#     random_str = str(random())
#     hex_str = hashlib.sha256(random_str).hexdigest()
#     return hex_str
#
#
# app.jinja_env.globals['csrf_token'] = generate_csrf_token
# app.secret_key = os.urandom(24)
