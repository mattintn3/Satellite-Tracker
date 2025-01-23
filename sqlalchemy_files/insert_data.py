import requests
from models import Satellite
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base


DATABASE_URL = "postgresql://postgres:password@127.0.0.1/satellites"
engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)
session = Session()

# Fetch the JSON data
json_url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=json"
response = requests.get(json_url)
json_data = response.json()

for sat in json_data:
    existing_satellite = session.query(Satellite).filter_by(object_name=sat["OBJECT_NAME"]).first()
    if existing_satellite:
        print(f"Skipping duplicate: {sat['OBJECT_NAME']}")
        continue
    
    satellite = Satellite(
        object_name=sat["OBJECT_NAME"],
        object_id=sat["OBJECT_ID"],
        epoch=sat["EPOCH"],
        mean_motion=sat["MEAN_MOTION"],
        eccentricity=sat["ECCENTRICITY"],
        inclination=sat["INCLINATION"],
        ra_of_asc_node=sat["RA_OF_ASC_NODE"],
        arg_of_pericenter=sat["ARG_OF_PERICENTER"],
        mean_anomaly=sat["MEAN_ANOMALY"],
        ephemeris_type=sat["EPHEMERIS_TYPE"],
        classification_type=sat["CLASSIFICATION_TYPE"],
        norad_cat_id=sat["NORAD_CAT_ID"],
        element_set_no=sat["ELEMENT_SET_NO"],
        rev_at_epoch=sat["REV_AT_EPOCH"],
        bstar=sat["BSTAR"],
        mean_motion_dot=sat["MEAN_MOTION_DOT"],
        mean_motion_ddot=sat["MEAN_MOTION_DDOT"]
    )
    session.add(satellite)

session.commit()
print("Satellites have been added to database succesfully!")
