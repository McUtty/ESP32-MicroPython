# How to - use DHT11 and show on Oled
from machine import Pin, I2C
import dht
import ssd1306

class OLEDDHT11:

    def __init__(self, sclPin, sdaPin, dhtPin, oledadd):
        self.sclPin = sclPin
        self.sdaPin = sdaPin
        self.dhtPin = dhtPin
        self.oledadd = oledadd

        self.i2c = I2C(scl=Pin(self.sclPin), sda=Pin(self.sdaPin))
        self.oled = ssd1306.SSD1306_I2C(128, 64, self.i2c, self.oledadd)

        self.dhtvalues = dht.DHT11(Pin(self.dhtPin))

    def displayhdt11(self):
        self.dhtvalues.measure()
        self.oled.fill(0)
        self.oled.text('Temp: {}'.format(self.dhtvalues.temperature()), 0, 30)
        self.oled.text('Luftf.: {}%'.format(self.dhtvalues.humidity()), 0, 40)
        self.oled.show()
