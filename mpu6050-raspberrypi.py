from mpu6050 import mpu6050
import time
mpu = mpu6050(0x68)

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

while True:
    print("Temp : "+str(mpu.get_temp()))
    print()

    accel_data = mpu.get_accel_data()
    print("Acc X : "+str((accel_data['x'] - init_accel_x)))
    print("Acc Y : "+str((accel_data['y'] - init_accel_y)))
    print("Acc Z : "+str((accel_data['z'] - init_accel_z)))
    print()

    gyro_data = mpu.get_gyro_data()
    print("Gyro X : "+str((gyro_data['x'] - init_gyro_data_x)))
    print("Gyro Y : "+str((gyro_data['y'] - init_gyro_data_y)))
    print("Gyro Z : "+str((gyro_data['z'] - init_gyro_data_z)))
    print()
    print("-------------------------------")
    time.sleep(1)