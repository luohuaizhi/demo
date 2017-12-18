from application.models import db
from pony.orm import sql_debug
from pony.orm import Required, Optional, PrimaryKey
from pony.orm import db_session, commit, select, get, delete
from datetime import datetime, date


class Admin(db.Entity):
    # id = PrimaryKey(int, auto=True)
    name = Required(str, 32)
    password = Required(str, 16)
    level = Optional(int, default=0)

    _table_ = 'admin'


class User(db.Entity):
    # id = PrimaryKey(int, auto=True)
    name = Required(str, 32)
    password = Required(str, 8)
    gender = Optional(bool, default=True)
    birthday = Optional(date, nullable=True)
    phone = Optional(str, 11, nullable=True)
    photo = Optional(buffer, nullable=True)
    register = Required(datetime, sql_default='CURRENT_TIMESTAMP')

    _table_ = 'user'


sql_debug(True)
db.generate_mapping(create_tables=True)


@db_session
def init_user():
    delete(u for u in User)
    User(name="test", password="123123")
    commit()
    users = select(u for u in User)
    return users.first()


@db_session
def init_admin():
    delete(u for u in Admin)
    User(name="admin", password="admin")
    commit()
    users = select(u for u in Admin)
    return users.first()


print init_user().register
print init_admin()
