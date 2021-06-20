from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from api.database import db, ma

class User(db.Model):

    # Define Table name
    __tablename__ = 'users'

    # Define column of table
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

    def __init__(self, name, email, password, is_admin):
        self.name = name
        self.email = email
        self.set_password(password)
        self.is_admin = is_admin

    # Save password wifh hash
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        # Apporopriate model properties for all schima
        model = User

    # Not show when it is dumped
    password = ma.auto_field(load_only=True)