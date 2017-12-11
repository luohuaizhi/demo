from flask import Blueprint, render_template, make_response

mod = Blueprint('general', __name__)


@mod.route('/')
def hello_world():
    mod.logger.info("Hello Web")
    return 'Hello Web!'


@mod.route('/index')
def index():
    print "123"
    return render_template('index.html', name="James")


@mod.route('/info/<username>')
def info(username):
    res = make_response(render_template('info.html', name=username), 200)
    res.headers['X-web-info'] = "James's first flask web"
    return res


@mod.route('/list')
def list_data():
    data = ['record'+str(i) for i in xrange(10)]
    return render_template('list.html', data=data)
