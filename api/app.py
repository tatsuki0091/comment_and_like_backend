from flask import Flask

from api.database import init_db
import api.models

def create_app():
    app = Flask(__name__)
    app.config.from_object('comment_and_like.config.Config')
    init_db(app)
    return app
app = create_app()