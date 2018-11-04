# How to - show Data from BMP180 on Oled
from bmp180 import BMP180
from machine import I2C, Pin
import ssd1306, time

class oledWEATHER:
    def __init__(self, scladd = 4, sdaadd = 5, bmpadd = 0x77, bmpfreq = 400000, oledadd = 0x3C):
        self.scladd = scladd
        self.sdaadd = sdaadd
        self.bmpadd = bmpadd
        self.bmpfreq = bmpfreq
        self.oledadd = oledadd

        self.i2c =  I2C(scl=Pin(self.scladd), sda=Pin(self.sdaadd), freq=self.bmpfreq)  #freq 100000 on esp8266
        self.bmp180 = BMP180(self.i2c)
        self.oled = ssd1306.SSD1306_I2C(128, 64, self.i2c, self.oledadd)    #0x3c

        self.bmp180.oversample_sett = 2
        self.bmp180.baseline = 102225   #101325


    def printweather(self):
        temp = self.bmp180.temperature
        p = self.bmp180.pressure / 100
        alti = self.bmp180.altitude

        self.oled.fill(0)
        self.oled.text('UT DataStation',0 ,0)
        self.oled.line(0,10,128,10,1)
        self.oled.text('Temp: {0}'.format(temp), 0, 20)
        self.oled.text('hPascal: {0}'.format(p), 0, 30)
        self.oled.text('High: {0}'.format(alti), 0, 40)
        self.oled.line(0,50,128,50,1)
        self.oled.show()


    def tempvalue(self):
        tempx = self.bmp180.temperature
        return  tempx

    def barovalue(self):
        barox = self.bmp180.pressure / 100
        return  barox

def main():
    print('Hallo')
    oledWEATHER.__init__(self)

if __name__ == '__main__':
    main()
