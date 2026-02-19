
class Config(object):
    SECRET_KEY='Clave nueva'
    SESSION_COOKIE_SECURE=False

class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URL='mysql+pymysql://root:Navarro49@127.0.0.1/idgs802'
    SQLALCHEMY_TRACK_MODIFICATIONS=False