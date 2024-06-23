# app.py

import json
import serial
import os
import initializeApp
import arduinoCore

# Загрузка настроек из config.json
with open('config.json', 'r') as f:
    config = json.load(f)

if __name__ == "__main__":
    ser = initializeApp.initializeApp(config)
    arduinoCore.read_serial_and_insert_data(ser, config)

#docker build -t arduino-log-app .
#запуск контейнера
#sudo docker run -it --rm --network="host" --device=/dev/ttyUSB0:/dev/ttyUSB0 arduino-log-app

