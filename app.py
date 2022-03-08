'''
Creating application factory for our app
'''


# Importing modules to use
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from flask_marshmallow import Marshmallow
from flask_cors import CORS

# Load config
env_config = os.getenv("APP_SETTINGS", "config.DevelopmentConfig")

# Globally accessible libraries
db = SQLAlchemy()
migrate = Migrate()
cors = CORS()

def create_app():
    """Initialize the code application."""
    app = Flask(__name__, instance_relative_config=False)
    
    # Load config from config files
    app.config.from_object(env_config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)

    return app
