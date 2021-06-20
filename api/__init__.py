from flask import Flask
from .database import init_db
from .models import User
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:admin@127.0.0.1:5432/buddytree'
db = SQLAlchemy(app)

app.config.from_object('config.Config')

init_db(app)