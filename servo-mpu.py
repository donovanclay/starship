from mpu6050 import mpu6050
import RPi.GPIO as GPIO
import time
import math

mpu = mpu6050(0x68)

# Set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)

# Set pin 11 as an output, and define as servo1 as PWM pin
GPIO.setup(11,GPIO.OUT)
servo1 = GPIO.PWM(11,50) # pin 11 for servo1, pulse 50Hz

# Start PWM running, with value of 0 (pulse off)
servo1.start(0)

# Calibrate 
init_temp = mpu.get_temp()

accel_data = mpu.get_accel_data()
init_accel_x = accel_data['x']
init_accel_y = accel_data['y']
init_accel_z = accel_data['z']

gyro_data = mpu.get_gyro_data()
init_gyro_data_x = gyro_data['x']
init_gyro_data_y = gyro_data['y']
init_gyro_data_z = gyro_data['z']

try:
    while True:
        # print("Temp : "+str(mpu.get_temp()))
        # print()

        # accel_data = mpu.get_accel_data()
        # print("Acc X : "+str((accel_data['x'] - init_accel_x)))
        # print("Acc Y : "+str((accel_data['y'] - init_accel_y)))
        # print("Acc Z : "+str((accel_data['z'] - init_accel_z)))
        # print()

        gyro_data = mpu.get_gyro_data()
        # print("Gyro X : "+str((gyro_data['x'] - init_gyro_data_x)))
        # print("Gyro Y : "+str((gyro_data['y'] - init_gyro_data_y)))
        # print("Gyro Z : "+str((gyro_data['z'] - init_gyro_data_z)))
        # print()
        # print("-------------------------------")
        # time.sleep(1)
        angle = abs((gyro_data['x'] - init_gyro_data_x))
        servo1.ChangeDutyCycle(2+(angle * 3/18))
        time.sleep(0.5)
        servo1.ChangeDutyCycle(0)

finally:
    #Clean things up at the end
    servo1.stop()
    GPIO.cleanup()
    print("Goodbye!")