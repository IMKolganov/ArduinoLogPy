# temp_humidity_repository.py

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models.tempHumidity import Base, TempHumidity
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime

engine = create_engine('postgresql://rackot:arduinologdb@127.0.0.1:5432/arduinologdb')
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)

def add_temp_humidity(humidity, temperature, error=None):
    session = Session()

    try:
        new_data = TempHumidity(humidity=humidity, temperature=temperature, error=error)
        session.add(new_data)
        session.commit()
        print(f"Data for TempHumidity successfully added: {new_data}")
    except SQLAlchemyError as e:
        print(f"Error inserting data for TempHumidity into the database: {e}")
        session.rollback()
    finally:
        session.close()

def get_temp_humidity_by_id(id):
    session = Session()

    try:
        data = session.query(TempHumidity).filter(TempHumidity.id == id).first()
        return data
    except SQLAlchemyError as e:
        print(f"Error retrieving data for TempHumidity from the database: {e}")
    finally:
        session.close()
