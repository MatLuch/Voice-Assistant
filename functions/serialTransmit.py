import serial
import time
from info import *

esp = serial.Serial(com, 115200)

time.sleep(2)  


def serialSend(text):
    esp.write((text + "\n").encode())

