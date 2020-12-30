from werkzeug.security import generate_password_hash, check_password_hash

class Config(object):

    SECRET_KEY = '8e422c119fcc0bdb1e78777d4febaaf7'

    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'demo_flask'

    SQLALCHEMY_DATABASE_URI = 'mysql://' + MYSQL_USER \
                            + ':' + MYSQL_PASSWORD \
                            + '@' + MYSQL_HOST \
                            + '/' + MYSQL_DB
    SQLALCHEMY_TRACK_MODIFICATIONS = False