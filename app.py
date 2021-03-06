from flask_cors import CORS
from api.database import init_db
from api.controllers.login import loginAuth
from api.controllers.comment import handleGetComment, handlePostComment
from api.controllers.like import handleIsFavorite, handleLikeCount, handleLike
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)

app.register_blueprint(loginAuth)
app.register_blueprint(handleGetComment)
app.register_blueprint(handlePostComment)
app.register_blueprint(handleLike)
app.register_blueprint(handleIsFavorite)
app.register_blueprint(handleLikeCount)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://lalzwszzkjnwwt:51b8bf34a4afc9e2030ffe0bd03ceda4dfa6ed7b9ff078eebeee30ff2741c0ed@ec2-18-211-97-89.compute-1.amazonaws.com:5432/dchqftr0o25nrg'
app.config['SQLALCHEMY_ECHO'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_object('config.Config')
app.config['CORS_HEADERS'] = 'Content-Type'
init_db(app)
db = SQLAlchemy(app)

CORS(app, origins=["http://localhost:3000/*", "https://localhost:3000/*", "https://boiling-dusk-58225.herokuapp.com/*", "http://boiling-dusk-58225.herokuapp.com/*"])

if __name__ == "__main__":
    app.run()



