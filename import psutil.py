import GPUtil
import time
import serial
ser = serial.Serial("COM11")
ser.baudrate = 115200
while True:
    gpus = GPUtil.getGPUs()
    for gpu in gpus:
        time.sleep(1)
        gpu_temperature = 't'+ str(int(gpu.temperature))
        print(gpu_temperature.encode('utf-8'))
        ser.write(50)
        