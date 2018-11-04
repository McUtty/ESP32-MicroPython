"""
We then have some methods to manage the display:

- poweroff(), turns off the screen. Convenient for battery operation.
- contrast(), to adjust the contrast
- invert(), invert the colors of the screen (finally white and black!)
- show(), to refresh the view
- fill(), to fill the screen in black (1) or white (0)
- pixel(), to turn on a particular pixel
- scroll(), scroll the screen.
- text(), to display on text at the indicated x, y position
- Draw lines hline(sx,sy,ex,ey,tl) - start-x, start-y, end-x, end-y, line thikness
- vline(sx,sy,ex,ey,tl) - start-x, start-y, end-x, end-y, line thikness
- a simple line line()
- Draw a rect rect rectangle() or rectangle filled fill_rect()
"""
import machine, ssd1306

i2c = machine.I2C(scl=machine.Pin(4), sda=machine.Pin(5))
oled = ssd1306.SSD1306_I2C(128, 64, i2c, 0x3c)

def Oled_Text(TText,TPositX,TPositY):
    oled.fill(0)
    oled.text(TText, TPositX, TPositY)
    oled.show()
