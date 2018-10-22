import os

class BaseConfig():
    """Set app config vars."""
    DEBUG = True
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = "sqlite:///../instance/flask-crud.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #SESSION_TYPE = null
    SESSION_COOKIE_NAME = 'session name'
    SESSION_PERMANENT = True
    #PERMANENT_SESSION_LIFETIME = timedelta(days=31) (2678400 seconds)

class ProductionConfig():
    """Set app config vars."""
    SECRET_KEY = os.urandom(24)
    #SESSION_TYPE = null
    SESSION_COOKIE_NAME = 'session name'
    SESSION_PERMANENT = True
    #PERMANENT_SESSION_LIFETIME = timedelta(days=31) (2678400 seconds)