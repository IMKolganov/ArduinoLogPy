# arduinoCore.py

from datetime import datetime
from repositories.soil_moisture_repository import SoilMoistureRepository
from repositories.temp_humidity_repository import TempHumidityRepository
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import serial
import psycopg2
import json

def read_serial_and_insert_data(ser, config):
    db_url = (
        f"postgresql://{config['db']['user']}:{config['db']['password']}"
        f"@{config['db']['host']}:{config['db']['port']}/{config['db']['name']}"
    )

    soil_moisture_repo = SoilMoistureRepository(db_url)
    temp_humidity_repo = TempHumidityRepository(db_url)

    try:
        while True:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8', errors='ignore').rstrip()
                print(line)

                if line:
                    try:
                        data = json.loads(line)
                        
                        if data['sensor'] == 'soil_moisture':
                            value = data.get('value', 0)
                            value = 0 if value < 0 else value
                            error = data.get('error')
                            
                            soil_moisture_repo.add_soil_moisture(value=value, error=error)

                        if data['sensor'] == 'temp_humidity':
                            humidity = data.get('humidity', 0)
                            humidity = 0 if humidity < 0 else humidity
                            temperature = data.get('temperature', 0)
                            temperature = 0 if temperature < 0 else temperature
                            error = data.get('error')

                            temp_humidity_repo.add_temp_humidity(humidity=humidity, temperature=temperature, error=error)
                    except json.JSONDecodeError:
                        print("Error decoding JSON")
                else:
                    print("Empty string, please check JSON")
    except KeyboardInterrupt:
        print("User terminated the program")
    except (serial.SerialException, psycopg2.Error) as e:
        print("Fatal error:", e)
        close_program()
