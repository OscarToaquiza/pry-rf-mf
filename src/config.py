from decouple import config


class Config:
    SECRET_KEY = config('SECRET_KEY')


class DevelomentConfig(Config):
    DEBUG = False


config = {
    'development': DevelomentConfig
}
