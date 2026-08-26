import serial
import time

esp = serial.Serial("COM9", 115200)

time.sleep(2)  


def serialSend(text):
    esp.write((str(text) + "\n").encode())

