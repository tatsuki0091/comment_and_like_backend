from flask import Flask

from api.database import init_db
import api.models
from flask_cors import CORS, cross_origin
from flask import Flask, Response, request, jsonify

# def create_app():
#     app = Flask(__name__)
#     CORS(app, origins=["http://localhost:3000"])
#     app.config.from_object('comment_and_like.config.Config')
#     app.config['CORS_HEADERS'] = 'Content-Type'
#     init_db(app)
#     return app
# app = create_app()

