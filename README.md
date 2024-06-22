# ArduinoLogPy

ArduinoLogPy — это проект для чтения данных с Arduino через последовательный порт и сохранения их в базу данных PostgreSQL.

## Сборка Docker-образа

Для создания Docker-образа выполните следующую команду:

docker build -t arduino-log-app .

## Запуск Docker-контейнера

Для запуска Docker-контейнера выполните следующую команду:

sudo docker run -it --rm --network="host" --device=/dev/ttyUSB0:/dev/ttyUSB0 arduino-log-app

## Структура проекта

ArduinoLogPy/

├── app.py

├── arduinoCore.py

├── db.py

├── requirements.txt

├── config.json

└── Dockerfile

app.py — основной скрипт для запуска приложения.
arduinoCore.py — модуль для работы с Arduino.
db.py — модуль для работы с базой данных PostgreSQL.
requirements.txt — файл с зависимостями Python.
config.json — файл конфигурации.
Dockerfile — Dockerfile для создания Docker-образа.

## Требования

- Docker
- PostgreSQL
- Arduino с подключением через последовательный порт

## Конфигурация

Проект использует файл `config.json` для настройки параметров подключения. Пример файла `config.json`:

```json
{
  "serial_port": "/dev/ttyUSB0",
  "serial_baudrate": 9600,
  "db": {
    "user": "your_db_user",
    "password": "your_db_password",
    "host": "127.0.0.1",
    "port": 5432,
    "name": "your_db_name"
  }
}
