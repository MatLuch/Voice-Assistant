import serial 
import time 

esp = serial.Serial("COM9", 115200)

time.sleep(2)

while True:
    command = input("enter: ")

    esp.write((command + "\n").encode())