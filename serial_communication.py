import serial

def connect_to_serial(port, baudrate):
    try:
        ser = serial.Serial(port, baudrate)
        return ser
    except serial.SerialException as e:
        print(f"Ошибка подключения к серийному порту: {e}")
        raise
