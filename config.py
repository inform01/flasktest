class Configuration(object):
    debug=True
    SQLALCHEMY_TRACK_MODIFICATIONS= False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:root@localhost/test1'
    SECRET_KEY = 'secret'

    ###flask_security

    SECURITY_PASSWORD_SALT = 'salt'
    SECURITY_PASSWORD_HASH = 'sha512_crypt'
