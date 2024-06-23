# repositories/soil_moisture_repository.py

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models.soilMoisture import Base, SoilMoisture
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime

class SoilMoistureRepository:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)
    
    def add_soil_moisture(self, value, error):
        session = self.Session()
        try:
            soil_moisture = SoilMoisture(value=value, error=error)
            session.add(soil_moisture)
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            print(f"Error adding soil moisture data: {e}")
        finally:
            session.close()
