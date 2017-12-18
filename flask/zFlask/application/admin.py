# -*- encoding:utf-8 -*-
from flask import Blueprint, url_for, render_template, request, flash
from pony.orm import get, select, db_session, commit
from application.models.model import Admin, User

mod = Blueprint('admin', __name__)


@mod.route('/', methods=['GET', 'POST'])
@db_session
def admin():
    if request.method == "GET":
        return render_template('admin/login.html', msg="")
    elif request.method == "POST":
        admin_name = request.form["admin"]
        password = request.form["password"]
        a = get(a for a in Admin if a.name == admin_name and password == password)
        if a and a.id:
            user_list = select(u for u in Admin)
            return render_template('admin/index.html', user_list=user_list)
        else:
            flash("auth failed!")
            return render_template('admin/login.html', msg="auth failed!")
    return render_template('base/500.html')


@mod.route('/index')
def index():
    user_list = select(u for u in User)
    return render_template('admin/index.html', user_list=user_list)


@mod.route('/modify')
@db_session
def add():
    name = request.get("admin")
    if name != "admin":
        return "Insufficient permissions"
    uid = request.get("id")
    name = request.get("name")
    pwd = request.get("password")
    u = select(u for u in User if u.id == uid)
    if u:
        u.name = name
        u.password = pwd
    else:
        User(name=name, password=pwd)
    commit()
    return url_for('.index')





