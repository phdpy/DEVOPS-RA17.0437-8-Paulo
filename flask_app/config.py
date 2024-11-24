import os

class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://flaskuser:1559@localhost/escola"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)
