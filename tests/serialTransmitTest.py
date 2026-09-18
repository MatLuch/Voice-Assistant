import serial 
import time 

esp = serial.Serial("COM3", 115200)

time.sleep(2)

print("Start entering what you want to send: ")

while True:
    x = input()
    command = str(x)

    esp.write((command + "\n").encode())