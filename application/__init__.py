from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# globally accessible libraries
db = SQLAlchemy()


def create_app():
    """ Initialize the core application """

    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")

    # initialize plugins
    db.init_app(app)

    with app.app_context():
        # in here are all the pieces of my program
        # 1] routes
        # 2] blueprints
        # whatever..  
        from application import routes
        db.create_all()

        return app