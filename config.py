# from email.policy import default
import os
# from decouple import config


class Config:

    SECRET_KEY = '123Qwe'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:////home/lona/Desktop/Pitches/pitches.db'
    SQLALCHEMY_DATABASE_URI = 'postgres://wlgqwfxagylxki:6a72382d05483c9fd71ab436bc5f83cba640191b59358ced9d608dd24b2cf8c3@ec2-3-229-11-55.compute-1.amazonaws.com:5432/d63mrtoduck209'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    # email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    DEBUG = True


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
