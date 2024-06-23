# repositories/temp_humidity_repository.py

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models.tempHumidity import Base, TempHumidity
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime

class TempHumidityRepository:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)
    
    def add_temp_humidity(self, humidity, temperature, error):
        session = self.Session()
        try:
            temp_humidity = TempHumidity(humidity=humidity, temperature=temperature, error=error)
            session.add(temp_humidity)
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            print(f"Error adding temp humidity data: {e}")
        finally:
            session.close()
