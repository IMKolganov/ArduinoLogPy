# app.py

import serial
import psycopg2  # Добавляем импорт модуля psycopg2
import db

serial_port = '/dev/ttyUSB0'
serial_baudrate = 9600
db_user = 'rackot'
db_password = 'arduinologdb'  # Укажите ваш реальный пароль здесь
db_host = '127.0.0.1'
db_port = '5432'
db_name = 'arduinologdb'

# Глобальные переменные для подключения
ser = None
connection = None
cursor = None

def initialize():
    global ser, connection, cursor

    try:
        # Подключение к серийному порту
        ser = serial.Serial(serial_port, serial_baudrate)
        print(f"Подключение к {serial_port} установлено.")

        # Подключение к PostgreSQL
        connection, cursor = db.connect_to_postgresql(db_user, db_password, db_host, db_port, db_name)
        print("Подключение к PostgreSQL установлено.")

        # Выполнение SQL-запроса для проверки подключения
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        print("Вы подключены к - ", record, "\n")

    except (serial.SerialException, psycopg2.Error) as e:
        print("Ошибка при инициализации:", e)
        close_program()

def read_serial_and_insert_data():
    try:
        while True:
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').rstrip()
                print(line)
                
                # Вставка данных в PostgreSQL
                db.insert_data(cursor, connection, line)

    except KeyboardInterrupt:
        print("Прерывание от пользователя")

    except (serial.SerialException, psycopg2.Error) as e:
        print("Ошибка во время работы программы:", e)
        close_program()

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
    initialize()
    read_serial_and_insert_data()
