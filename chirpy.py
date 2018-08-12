from time import sleep
import machine
import ustruct

#Init I2C
iic = machine.I2C(scl=machine.Pin(4), sda=machine.Pin(5), freq=30000)

#Ohne chirlib ...
#Capacitance von Chirp auslesen
chcap = iic.readfrom_mem(0x20,0x00,2)
print("Feuchtigkeit: ",+ ustruct.unpack('>H', chcap)[0])
sleep(1)

#Addresse von Chirp auslesen
chadd = iic.readfrom_mem(0x20,0x02,1)[0]
print("Addresse: ",+ chadd)
sleep(1)

#Temperatur auslesen
chtemp = iic.readfrom_mem(0x20,0x05,2)
print("Temperatur: ",+ ustruct.unpack('>H', chtemp)[0] / 10)
sleep(1)

#LichtLevel auslesen
iic.writeto_mem(0x20, 0x03, b'0')
sleep(5)
chlight = iic.readfrom_mem(0x20,0x04,2)
print("LichtLevel: ",+ ustruct.unpack('>H', chlight)[0])
