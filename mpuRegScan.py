from machine import I2C, Pin
from time import sleep_ms
import mpu6050

i2c = I2C(scl=Pin(4), sda=Pin(5))

accelerometer = mpu6050.accel(i2c, 0x68)

count = 13

while (count <= 117):
    scale = accelerometer.read_scale(count)
    print('{}-{}'.format(hex(count), scale))
    count += 1
    sleep_ms(500)


#0x40-b't\xee\xb0\xfc2\xff\x9c\xff'
#0x41-b'\xee\xd0\xfcC\xff\x8a\xff\xf0'
