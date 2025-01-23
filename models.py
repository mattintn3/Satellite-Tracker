import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy as FlaskSQLAlchemy
from flask_marshmallow import Marshmallow


metadata = db.MetaData()
Base = declarative_base(metadata=metadata)
    
class User(Base):
    __tablename__ = 'users'
    id = db.Column(db.String, primary_key=True, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, unique=False, nullable=False)
    totp = db.Column(db.Boolean, unique=False, nullable=False, server_default="0")
    totpSecret = db.Column(db.String, unique=False, nullable=True)
    active = db.Column(db.Boolean, unique=False, nullable=False, server_default="0")
    created = db.Column(db.DateTime, unique=False, nullable=False)
    lastActivity = db.Column(db.DateTime, unique=False, nullable=True)
    IsAdmin = db.Column(db.Boolean, unique=False, nullable=False, server_default="0")
    isBanned = db.Column(db.Boolean, unique=False, nullable=False, server_default="0")

class Usernames(Base):
    __tablename__ = 'usernames'
    id = db.Column(db.String, primary_key=True, unique=True, nullable=False)
    username = db.Column(db.String, unique=True, nullable=False)
    userid = db.Column(db.String, db.ForeignKey('users.id'), nullable=False)
    timestamp = db.Column(db.DateTime, unique=False, nullable=False)