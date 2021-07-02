from flask import Flask

from api.database import init_db
from flask_cors import CORS
from flask import Flask

def create_app():
    app = Flask(__name__)
    CORS(app, origins=["https://mysterious-citadel-26921.herokuapp.com*", "http://localhost:3000*"])
    app.config['CORS_HEADERS'] = 'Content-Type'
    app.config.from_object('comment_and_like.config.Config')
    init_db(app)
    return app
app = create_app()