import os

class DevelopmentConfig:

    # Flask
    ENV = 'development'
    DEBUG = True

    # SQLALCHEMY_DATABASE_URI = 'postgresql://admin:admin@127.0.0.1:5432/buddytree'
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_ECHO = False

Config = DevelopmentConfig