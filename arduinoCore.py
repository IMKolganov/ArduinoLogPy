from datetime import datetime
from repositories.soil_moisture_repository import add_soil_moisture
from repositories.temp_humidity_repository import add_temp_humidity
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import serial
import psycopg2
import json

def read_serial_and_insert_data(ser, config):
    try:
        while True:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').rstrip()
                print(line)

                if line:
                    try:
                        data = json.loads(line)
                        
                        # Check sensor "soil_moisture"
                        if data['sensor'] == 'soil_moisture':
                                value = data.get('value', 0)
                                value = 0 if value < 0 else value
                                error = data.get('error')

                                # Create an engine and session
                                db_url = (
                                f"postgresql://{config['db']['user']}:{config['db']['password']}"
                                f"@{config['db']['host']}:{config['db']['port']}/{config['db']['name']}"
                                )
                                
                                add_soil_moisture(value=value, error=error)
                        # Check sensor "temp_humidity"
                        if data['sensor'] == 'temp_humidity':
                                humidity = data.get('humidity', 0)
                                humidity = 0 if humidity < 0 else humidity
                                temperature = data.get('temperature', 0)
                                temperature = 0 if temperature < 0 else temperature
                                error = data.get('error')

                                # Create an engine and session
                                db_url = (
                                f"postgresql://{config['db']['user']}:{config['db']['password']}"
                                f"@{config['db']['host']}:{config['db']['port']}/{config['db']['name']}"
                                )
                                
                                add_temp_humidity(humidity=humidity, temperature=temperature, error=error)

                                #db.insert_data(cursor, connection, line)
                    except json.JSONDecodeError:
                        print("Error decode JSON")
                else:
                    print("Empty string Please check json")
    except KeyboardInterrupt:
        print("User terminate program")

    except (serial.SerialException, psycopg2.Error) as e:
        print("Fatal error:", e)
        close_program()
