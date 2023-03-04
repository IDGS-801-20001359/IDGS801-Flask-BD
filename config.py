import os

from sqlalchemy import create_engine

import urllib
class Config(object):
    SECRET_KEY='MV_SECRET_KEY'
    SESSION_COOKIE_SECURE=False

class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:@localhost:3306/idgs-801'
    SQLALCHEMY_TRACK_MODIFICATION=False
