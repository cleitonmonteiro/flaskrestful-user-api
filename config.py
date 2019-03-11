import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """
    Common configurations
    """
    
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'p9Bv<3Eid9%$i01'
    SQLALCHEMY_ECHO = True


class DevelopmentConfig(Config):
    """
    Development configurations
    """

    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG                   = False
    SQLALCHEMY_ECHO         = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')


class TestingConfig(Config):
    """
    Testing configurations
    """

    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')
    

app_config = {
    'default': DevelopmentConfig,
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
