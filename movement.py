from machine import I2C, Pin
import mpu6050, ssd1306
from time import sleep_ms

class MOVEMENT():

    def __init__(self, sclPin, sdaPin, accadd, oledadd):
        self.sclPin = sclPin
        self.sdaPin = sdaPin
        self.oledadd = oledadd
        self.accadd = accadd

        #print('{}-{}-{}-{}' .format(self.sclPin, self.sdaPin, self.oledadd, self.accadd))

        self.i2c = I2C(scl=Pin(self.sclPin), sda=Pin(self.sdaPin))
        self.oled = ssd1306.SSD1306_I2C(128, 64, self.i2c, self.oledadd)

        self.accelerometer = mpu6050.accel(self.i2c, self.accadd)

        self.accelerometer.set_frs_ac(3)

        self.scale = self.accelerometer.read_scale(0x1C)
        print(self.scale)

    def acx_value(self):

        movex = 0

        for i in range(10):
            move = self.accelerometer.get_values()
            movex = movex + int(move["AcX"])
            sleep_ms(20)

        movex = movex / 10

        self.oled.fill(0)
        self.oled.text('AcX {}'.format(movex), 0, 30)
        self.oled.show()
        #sleep_ms(50)

    #acx_value()


"""
Beispiel
for value in k.values():
     print value

for key, value in k.items():
     print key, value

print('{0}'.format(scale))
"""
