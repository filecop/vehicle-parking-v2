import os
class BaseConfig:
    SECRET_KEY=os.getenv("SECRET_KEY","change-this")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = True
    TESTING = False

class DevConfig(BaseConfig):
    DEBUG = True

class ProdConfig(BaseConfig):
    pass

class TestConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv("TEST_DATABASE_URL", "sqlite:///:memory:")