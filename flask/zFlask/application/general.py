# -*- encoding:utf-8 -*-
from flask import Blueprint, render_template, redirect, url_for, request, sessions, flash
from pony.orm import get, db_session
from application.models.model import User
import json

mod = Blueprint('general', __name__)


@mod.route('/')
def hello_world():
    return redirect('/index')


@mod.route('/index')
def index(user=None):
    if not user:
        return render_template('login.html')
    return render_template('index.html', user=user)


@mod.route('/login', methods=['GET', 'POST'])
@db_session
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        u = get(u for u in User if u.name == username and u.password == password)
        if u:
            return render_template('index.html', user=u)
        else:
            flash("auth failed")
    return render_template('login.html')

