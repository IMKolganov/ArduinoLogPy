import psycopg2
from psycopg2 import sql

def connect_to_postgresql(config):
    try:
        connection = psycopg2.connect(
            user=config["db"]["user"],
            password=config["db"]["password"],
            host=config["db"]["host"],
            port=config["db"]["port"],
            dbname=config["db"]["name"]
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
