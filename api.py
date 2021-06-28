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
CORS(app, origins=["http://localhost:3000*"])

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:admin@127.0.0.1:5432/buddytree'
app.config['SQLALCHEMY_ECHO'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_object('config.Config')
app.config['CORS_HEADERS'] = 'Content-Type'
init_db(app)
db = SQLAlchemy(app)


@app.route('/')
def index():
    return 'Hello World!'

if __name__ == "__main__":
    app.run(host="0.0.0.0")


# if __name__ == '__main__':
#     application.run()


