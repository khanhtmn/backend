"""
This module is used to run deployment tasks
and to update the database
"""


def deploy():
    """Run deployment tasks."""

    # Import necessary files and packages
    from app import create_app, db
    from flask_migrate import upgrade, migrate, init, stamp
    from models import Login, UserProject

    # Create application context
    app = create_app()
    app.app_context().push()

    # Create database and tables
    db.create_all() 

    # Migrate database to latest
    stamp()
    migrate()
    upgrade()

deploy()
