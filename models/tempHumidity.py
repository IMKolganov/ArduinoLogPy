from sqlalchemy import Column, Integer, Float, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class TempHumidity(Base):
    __tablename__ = 'temp_humidity'

    id = Column(Integer, primary_key=True, autoincrement=True)
    humidity = Column(Float)
    temperature = Column(Float)
    error = Column(String)
    create_date = Column(DateTime(timezone=True), default=func.now())

    def __repr__(self):
        return f"<TempHumidity(id={self.id}, humidity={self.humidity}, temperature={self.temperature}, error={self.error}, create_date={self.create_date})>"
