from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow, fields
from flask_migrate import Migrate

db = SQLAlchemy()
ma = Marshmallow()

fields = fields.fields

# To represent SQL on the log
# import logging
# logging.basicConfig()
# logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)


def init_db(app):
    db.init_app(app)
    Migrate(app, db)