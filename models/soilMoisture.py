from sqlalchemy import Column, Integer, Float, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class SoilMoisture(Base):
    __tablename__ = 'soil_moisture'

    id = Column(Integer, primary_key=True, autoincrement=True)
    value = Column(Float)
    error = Column(String)
    create_date = Column(DateTime(timezone=True), default=func.now())

    def __repr__(self):
        return f"<SoilMoisture(id={self.id}, value={self.value}, error={self.error}, create_date={self.create_date})>"
