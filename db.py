import psycopg2
from psycopg2 import sql

def connect_to_postgresql(user, password, host, port, dbname):
    try:
        connection = psycopg2.connect(
            user=user,
            password=password,
            host=host,
            port=port,
            dbname=dbname
        )
        cursor = connection.cursor()
        return connection, cursor
    except psycopg2.Error as e:
        print(f"Ошибка подключения к базе данных PostgreSQL: {e}")
        raise

def insert_data(cursor, connection, data):
    try:
        insert_query = sql.SQL("INSERT INTO test (data_column) VALUES (%s)")
        cursor.execute(insert_query, (data,))
        connection.commit()
    except psycopg2.Error as e:
        print(f"Ошибка вставки данных в базу данных PostgreSQL: {e}")
        connection.rollback()
        raise
