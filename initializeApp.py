# initializeApp.py

import json
import serial
import psycopg2
import db

def initializeApp(config):
    ser = None
    connection = None
    cursor = None

    try:
        serial_port = config["serial_port"]
        serial_baudrate = config["serial_baudrate"]

        # Подключение к серийному порту
        ser = serial.Serial(serial_port, serial_baudrate)
        print(f"Подключение к {serial_port} установлено.")

        # Подключение к PostgreSQL
        connection, cursor = db.connect_to_postgresql(config)
        print("Подключение к PostgreSQL установлено.")

        # Выполнение SQL-запроса для проверки подключения
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        print("Вы подключены к - ", record, "\n")

        return ser, connection, cursor

    except (serial.SerialException, psycopg2.Error) as e:
        print("Ошибка при инициализации:", e)
        close_program(ser, connection, cursor)
        return None, None, None

def close_program(ser, connection, cursor):
    # Закрытие соединений
    if ser:
        ser.close()
        print("Соединение с серийным портом закрыто.")
    if connection and cursor:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто.")
