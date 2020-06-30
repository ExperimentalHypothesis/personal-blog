import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))


class Config:
    """ Class than holds configuration variables """

    # general config 
    SECRET_KEY = os.environ.get("SECRET_KEY")
    ENV = os.environ.get("ENV")

    # form config
    # TODO captcha

    # database config
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    
if __name__ == "__main__":
    pass