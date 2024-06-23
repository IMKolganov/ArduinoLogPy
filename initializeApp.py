# initializeApp.py

import json
import serial

def initializeApp(config):
    ser = None

    try:
        serial_port = config["serial_port"]
        serial_baudrate = config["serial_baudrate"]

        # Try to connect with arduino
        ser = serial.Serial(serial_port, serial_baudrate)
        print(f"Connect with {serial_port} successful.")

        return ser

    except (serial.SerialException) as e:
        print("Error initialization program", e)
        close_program(ser)
        return None
        
def close_program(ser):
    # Close connection
    if ser:
        ser.close()
        print("Disconected with adruino")
