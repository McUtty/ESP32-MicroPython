import oledweather
import movement
from time import sleep_ms
import esptouchsw
import machine
import oleddht11
import mqttclient


oledmovex = movement.MOVEMENT(4, 5, 0x68, 0x3C)
weather = oledweather.oledWEATHER(4, 5, 0x77, 400000, 0x3C)
tswitch = esptouchsw.ESPTOUCHSW(12)
displaydht = oleddht11.OLEDDHT11(4, 5, 15, 0x3C)
#publicweather = mqttclient.mqttPUBLIC()


while 1:

    while not .01 < tswitch.one_touchvalue() < .95:
        oledmovex.acx_value()
        sleep_ms(100)
    sleep_ms(1000)

    while not .01 < tswitch.one_touchvalue() < .95:
        sleep_ms(1000)
        weather.printweather()
        sleep_ms(1000)
        #publicweather.publictemp()
        #publicweather.publicbaro()
        #sleep_ms(1000)
        #print('Hallo')

    sleep_ms(1000)

    while not .01 < tswitch.one_touchvalue() < .95:
        displaydht.displayhdt11()
        sleep_ms(1200)

    sleep_ms(1000)
