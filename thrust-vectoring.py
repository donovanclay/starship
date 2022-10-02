# Link for mpu6050 instuctions: https://circuitdigest.com/microcontroller-projects/mpu6050-gyro-sensor-interfacing-with-raspberry-pi

# Import libraries
import RPi.GPIO as GPIO
import time
import smbus

# Set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)

# Set pin 11 as an output, and define as servo1 as PWM pin
GPIO.setup(11,GPIO.OUT)
servo1 = GPIO.PWM(11,50) # pin 11 for servo1, pulse 50Hz

# Start PWM running, with value of 0 (pulse off)
servo1.start(0)

# Initialize and calibrate bus for 12C
PWR_M   = 0x6B
DIV   = 0x19
CONFIG       = 0x1A
GYRO_CONFIG  = 0x1B
INT_EN   = 0x38
ACCEL_X = 0x3B
ACCEL_Y = 0x3D
ACCEL_Z = 0x3F
GYRO_X  = 0x43
GYRO_Y  = 0x45
GYRO_Z  = 0x47
TEMP = 0x41
bus = smbus.SMBus(1)

Device_Address = 0x68   # device address
AxCal=0
AyCal=0
AzCal=0
GxCal=0
GyCal=0
GzCal=0

# Initialize the mpu6050 module

def InitMPU():
    bus.write_byte_data(Device_Address, DIV, 7)
    bus.write_byte_data(Device_Address, PWR_M, 1)
    us.write_byte_data(Device_Address, CONFIG, 0)
    bus.write_byte_data(Device_Address, GYRO_CONFIG, 24)
    bus.write_byte_data(Device_Address, INT_EN, 1)
    time.sleep(1)

# Function to read data from mpu 
def readMPU(addr):
    high = bus.read_byte_data(Device_Address, addr)
    low = bus.read_byte_data(Device_Address, addr+1)
    value = ((high << 8) | low)
    if(value > 32768):
        value = value - 65536
    return value

# Read acceleration data
def accel():
    x = readMPU(ACCEL_X)
    y = readMPU(ACCEL_Y)
    z = readMPU(ACCEL_Z)

    Ax = (x/16384.0-AxCal)
    Ay = (y/16384.0-AyCal)
    Az = (z/16384.0-AzCal)
    #print "X="+str(Ax)
    time.sleep(.01)

# Read gyroscope data 
def gyro(): 
    global GxCal
    global GyCal
    global GzCal

    x = readMPU(GYRO_X)
    y = readMPU(GYRO_Y)
    z = readMPU(GYRO_Z)

    Gx = x/131.0 - GxCal
    Gy = y/131.0 - GyCal
    Gz = z/131.0 - GzCal
    #print "X="+str(Gx)
    time.sleep(.01)

# Callibrate mpu 
def calibrate():

    Print("Calibrate....")

    global AxCal
    global AyCal
    global AzCal

    x=0
    y=0
    z=0

    for i in range(50):
        x = x + readMPU(ACCEL_X)
        y = y + readMPU(ACCEL_Y)
        z = z + readMPU(ACCEL_Z)

    x= x/50
    y= y/50
    z= z/50

    AxCal = x/16384.0
    AyCal = y/16384.0
    AzCal = z/16384.0

    print(AxCal)
    print(AyCal)
    print(AzCal)

    global GxCal
    global GyCal
    global GzCal

    x=0
    y=0
    z=0

    for i in range(50):
        x = x + readMPU(GYRO_X)
        y = y + readMPU(GYRO_Y)
        z = z + readMPU(GYRO_Z)

    x= x/50
    y= y/50
    z= z/50

    GxCal = x/131.0
    GyCal = y/131.0
    GzCal = z/131.0

    print(GxCal)
    print(GyCal)
    print(GzCal)

# MAIN
InitMPU()
calibrate()


# Loop to allow user to set servo angle. Try/finally allows exit
# with execution of servo.stop and GPIO cleanup :)

# try:
#     while True:
#         #Ask user for angle and turn servo to it
#         angle = float(input('Enter angle between 0 & 180: '))
#         servo1.ChangeDutyCycle(2+(angle/18))
#         time.sleep(0.5)
#         servo1.ChangeDutyCycle(0)

# finally:
#     #Clean things up at the end
#     servo1.stop()
#     GPIO.cleanup()
#     print("Goodbye!")


