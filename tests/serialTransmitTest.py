import serial 
import time 

esp = serial.Serial("COM9", 115200)

time.sleep(2)

while True:
    x = input()
    command = str(x)

    esp.write((command + "\n").encode())