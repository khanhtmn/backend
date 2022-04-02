"""
Define models for database schema
"""

# from sqlalchemy.sql import func
    
from sqlalchemy import func, Index, text
from sqlalchemy.sql.operators import op
from sqlalchemy.orm import relationship

from datetime import datetime

from app import db

CONFIG = 'english'

# Create tsvector for Postgres fulltext search
def to_tsvector_ix(*columns):
    s = " || ' ' || ".join(columns)
    return func.to_tsvector(CONFIG, text(s))

def create_tsvector(*args):
    field, weight = args[0]
    exp = func.setweight(func.to_tsvector(CONFIG, field), weight)
    for field, weight in args[1:]:
        exp = op(exp, '||', func.setweight(func.to_tsvector(CONFIG, field), weight))
    return exp

class Login(db.Model):
    """
    Class defining model for user to log in
    """

    __tablename__ = 'logins'

    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String())
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128)) # hashed_password

    def __repr__(self):
        return '<Login info {}>'.format(self.email)

class UserProject(db.Model):
    """
    Class defining model for user info and their Capstone project
    """

    __tablename__ = 'user_projects'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("logins.id"))
    name = db.Column(db.String(128))
    class_year = db.Column(db.Integer)
    primary_major = db.Column(db.String(128))
    secondary_major = db.Column(db.String(128))
    primary_concentration = db.Column(db.String(256))
    secondary_concentration = db.Column(db.String(256))
    special_concentration = db.Column(db.String())
    minor = db.Column(db.String(128))
    minor_concentration = db.Column(db.String(256))
    

    title = db.Column(db.String())
    abstract = db.Column(db.String())
    project_link = db.Column(db.String())
    keywords = db.Column(db.String())
    feature = db.Column(db.String())
    hsr_review = db.Column(db.String())
    skills = db.Column(db.String())
    los = db.Column(db.String())
    custom_los = db.Column(db.String())
    advisor = db.Column(db.String())
    skills_offering = db.Column(db.String())
    skills_requesting = db.Column(db.String())
    location = db.Column(db.String())
    last_updated = db.Column(db.DateTime, index=True, default=datetime.utcnow().strftime('%m/%d/%Y %H:%M:%S'))

    logins = relationship(Login)

    # Define the tsvector for Postgres fulltext search
    __ts_vector__ = to_tsvector_ix(
        'name', 'primary_major', 'secondary_major', 'primary_concentration', 'secondary_concentration', 'special_concentration', 'minor', 'minor_concentration',
        'title', 'abstract', 'keywords', 'feature', 'hsr_review', 'skills', 'los', 'custom_los', 'advisor', 'skills_offering', 'skills_requesting', 'location',
    )

    __table_args__ = (
        Index('project_index', __ts_vector__, postgresql_using='gin'),
    )

    def __repr__(self):
        return '<User capstone info {}: {}>'.format(self.name, self.title)
