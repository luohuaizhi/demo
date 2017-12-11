# -*- encoding:utf-8 -*-
from app import app, admin, general

port = 5000
ip = ""
debug = True


if __name__ == "__main__":
    app.register_blueprint(general.mod)
    app.register_blueprint(admin.mod)
    app.run(ip=ip, port=port, debug=debug)
