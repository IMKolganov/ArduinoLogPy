from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tempHumidity import Base, TempHumidity
from soilMoisture import Base, SoilMoisture

# PostgreSQL connection string format:
# 'postgresql://username:password@host:port/database_name'
# Replace with your actual PostgreSQL credentials
DATABASE_URL = 'postgresql://rackot:arduinologdb@127.0.0.1:5432/arduinologdb'

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Bind the engine to the metadata of the Base class so that the declaratives can be accessed through a DBSession instance
Base.metadata.create_all(engine)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a Session instance
session = Session()

# Example of adding data
temp_humidity_data = TempHumidity(humidity=60.0, temperature=25.5, error=None)
session.add(temp_humidity_data)
soil_moisture_data = SoilMoisture(value=500.0, error=None)
session.add(soil_moisture_data)

# Commit the transaction
session.commit()

# Close the session
session.close()

print("Database and tables successfully created.")

# python create_db.py for run

# todo: not for now but need check (migration)
# pip install alembic
# alembic init alembic
