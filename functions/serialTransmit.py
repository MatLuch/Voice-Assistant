import serial
import time

esp = serial.Serial("COM3", 115200)

time.sleep(2)  


def serialSend(text):
    esp.write((text + "\n").encode())

