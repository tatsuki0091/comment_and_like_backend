from flask_cors import CORS
from api.database import init_db
from api.controllers.login import loginAuth
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)

app.register_blueprint(loginAuth)
CORS(app, origins=["http://localhost:3000*"])

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:admin@127.0.0.1:5432/buddytree'
app.config['SQLALCHEMY_ECHO'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_object('config.Config')
app.config['CORS_HEADERS'] = 'Content-Type'
init_db(app)



db = SQLAlchemy(app)


# SQLALCHEMY_DATABASE_URI = 'postgresql://admin:admin@127.0.0.1:5432/buddytree'
# SQLALCHEMY_TRACK_MODIFICATIONS = False
# SQLALCHEMY_ECHO = False


@app.route('/good')
def good():
    name = "Good"
    return name

if __name__ == "__main__":
    app.run()


# if __name__ == '__main__':
#     application.run()


