# arduinoCore.py

import serial
import db
import psycopg2

def read_serial_and_insert_data(ser, connection, cursor):
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
