import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy as FlaskSQLAlchemy
from flask_marshmallow import Marshmallow


metadata = db.MetaData()
Base = declarative_base(metadata=metadata)
    
class Satellite(Base):
    __tablename__ = 'satellites'
    object_name = db.Column(db.String, primary_key=True, unique=True, nullable=False)
    object_id = db.Column(db.String, unique=True, nullable=False)
    epoch = db.Column(db.DateTime, unique=False, nullable=False)
    mean_motion = db.Column(db.Double, unique=False, nullable=False, server_default="0")
    eccentricity = db.Column(db.Double, unique=False, nullable=True, server_default="0")
    inclination = db.Column(db.Double, unique=False, nullable=False, server_default="0")
    ra_of_asc_node = db.Column(db.Double, unique=False, nullable=False, server_default="0")
    arg_of_pericenter = db.Column(db.Double, unique=False, nullable=True, server_default="0")
    mean_anomaly = db.Column(db.Double, unique=False, nullable=False, server_default="0")
    ephemeris_type = db.Column(db.Boolean, unique=False, nullable=False, server_default="0")
    classification_type = db.Column(db.String, unique=False, nullable=False)
    norad_cat_id = db.Column(db.Integer, unique=False, nullable=False, server_default="0")
    element_set_no = db.Column(db.Integer, unique=False, nullable=False, server_default="0")
    rev_at_epoch = db.Column(db.Integer, unique=False, nullable=False, server_default="0")
    bstar = db.Column(db.Double, unique=False, nullable=False, server_default="0")
    mean_motion_dot = db.Column(db.Double, unique=False, nullable=False, server_default="0")
    mean_motion_ddot = db.Column(db.Double, unique=False, nullable=False, server_default="0")
#class Usernames(Base):
#    __tablename__ = 'usernames'
#    id = db.Column(db.String, primary_key=True, unique=True, nullable=False)
#    username = db.Column(db.String, unique=True, nullable=False)
#    userid = db.Column(db.String, db.ForeignKey('users.id'), nullable=False)
#    timestamp = db.Column(db.DateTime, unique=False, nullable=False)