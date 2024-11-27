class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///factory_management.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
