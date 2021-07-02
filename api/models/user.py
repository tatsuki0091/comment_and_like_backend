from datetime import datetime
from werkzeug.security import check_password_hash
from api.database import db, ma
from .comment import Comment
from .like import Like

class User(db.Model):

    # Define Table name
    __tablename__ = 'users'

    # Define column of table
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
    like = db.relationship(Like, backref='users', uselist=False)
    comment = db.relationship(Comment, backref='users', uselist=False)

    def __init__(self, email, password):
        self.email = email
        self.set_password(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        # Apporopriate model properties for all schima
        model = User

    # Not show when it is dumped
    password = ma.auto_field(load_only=True)