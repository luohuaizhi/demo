from flask import g, Blueprint, abort, redirect, url_for

mod = Blueprint('admin', __name__)


@mod.route('/admin')
def admin():
    return redirect(url_for('auth_admin'))


@mod.route('/auth_admin')
def auth_admin():
    abort(401)


@mod.route('/error')
def make_error():
    mod.logger.info("make a error")
    return 2/0  # make a ZeroDivisionError: integer division or modulo by zero


def after_this_request(f):
    if not hasattr(g, 'after_request_callbacks'):
        g.after_request_callbacks = []
    g.after_request_callbacks.append(f)
    return f


