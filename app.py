'''
Creating application factory for our app
'''


# Importing modules to use
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from flask_marshmallow import Marshmallow
from flask_cors import CORS

# Globally accessible libraries
db = SQLAlchemy()
migrate = Migrate()
# ma = Marshmallow()
cors = CORS()

def create_app():
    """Initialize the code application."""
    app = Flask(__name__, instance_relative_config=False)
    
    # Load config from config files
    app.config.from_pyfile('config.py')

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    # ma.init_app(app)
    cors.init_app(app)

    return app
