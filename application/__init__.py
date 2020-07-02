from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

# globally accessible libraries
db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()


def create_app():
    """ Initialize the core application """

    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")

    # initialize plugins
    db.init_app(app)
    login_manager.init_app(app)
    bcrypt = Bcrypt(app)
    
    with app.app_context():
        # in here are all the pieces of my program
        # 1] routes
        # 2] blueprints
        # whatever..  
        from application import routes       
        from application import routes_admin


        db.create_all()

        return app