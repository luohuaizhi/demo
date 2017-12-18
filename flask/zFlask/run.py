# -*- encoding:utf-8 -*-
from application import app, admin, general

host = "localhost"
port = 5000
debug = True


def run():
    app.register_blueprint(admin.mod, url_prefix="/admin")
    app.register_blueprint(general.mod)
    app.host = host
    app.port = port
    app.debug = debug
    app.run(host=host, port=port, debug=debug)


if __name__ == "__main__":
    run()

