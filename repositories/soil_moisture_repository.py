# soil_moisture_repository.py

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models.soilMoisture import Base, SoilMoisture
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime

engine = create_engine('postgresql://rackot:arduinologdb@127.0.0.1:5432/arduinologdb')
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)

def add_soil_moisture(value, error=None):
    session = Session()

    try:
        new_data = SoilMoisture(value=value, error=error)
        session.add(new_data)
        session.commit()
        print(f"Data for SoilMoisture successfully added: {new_data}")
    except SQLAlchemyError as e:
        print(f"Error inserting data for SoilMoisture into the database: {e}")
        session.rollback()
    finally:
        session.close()

def get_soil_moisture_by_id(id):
    session = Session()

    try:
        data = session.query(SoilMoisture).filter(SoilMoisture.id == id).first()
        return data
    except SQLAlchemyError as e:
        print(f"Error retrieving data for SoilMoisture from the database: {e}")
    finally:
        session.close()
