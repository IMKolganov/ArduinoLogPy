# app.py

import json
import serial
import psycopg2
import db
import os
import initializeApp
import arduinoCore

# Загрузка настроек из config.json
with open('config.json', 'r') as f:
    config = json.load(f)

serial_port = config["serial_port"]
serial_baudrate = config["serial_baudrate"]

# Глобальные переменные для подключения
ser = None
connection = None
cursor = None

def close_program():
    global ser, connection, cursor

    # Закрытие соединений
    if ser:
        ser.close()
        print("Соединение с серийным портом закрыто.")
    if connection and cursor:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто.")

if __name__ == "__main__":
    ser, connection, cursor = initializeApp.initializeApp(config)
    arduinoCore.read_serial_and_insert_data(ser, connection, cursor)
