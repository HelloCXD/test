
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class Baseconfig():
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #秘钥

    SECRET_KEY = '$%^&*(DFGHJKfgyu12312qd132213%^&*('

class Developconfig(Baseconfig):
    # SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(BASE_DIR, 'develop.db')
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/flask09'



config={
    'develop': Developconfig,
    'default': Developconfig,
}

def init_app(app, env_name):

    app.config.from_object(config.get(env_name))