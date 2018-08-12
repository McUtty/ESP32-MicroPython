from machine import Pin, TouchPad
from time import sleep

class ESPTOUCHSW():

    def __init__(self, tpin):
        self.tpin = tpin
        self.touch5 = TouchPad(Pin(self.tpin))
        self.threshold5 = []

        # Scan each TouchPad 12 times for calibration
        for x in range(12):
            self.threshold5.append(self.touch5.read())
            sleep(.1)

        # Store average threshold values
        self.threshold5 = sum(self.threshold5) / len(self.threshold5)
        print('Threshold5: {0}'.format(self.threshold5))



    def wait_touchvalue(self):

        while True:
            self.capacitance5 = self.touch5.read()
            self.cap_ratio5 = self.capacitance5 / self.threshold5
            # Check if a TouchPad is pressed
            if .40 < self.cap_ratio5 < .95:
                #player.next()
                print('Touch5: {0}, Diff: {1}, Ratio: {2}%.'.format(
                      self.capacitance5, self.threshold5 - self.capacitance5, self.cap_ratio5 * 100))
                sleep(.2)  # Debounce press
                return self.threshold5 - self.capacitance5

                break


    def one_touchvalue(self):

        self.capacitance5 = self.touch5.read()
        self.cap_ratio5 = self.capacitance5 / self.threshold5
        print('Touch5: {0}, Diff: {1}, Ratio: {2}%.'.format(self.capacitance5, self.threshold5 - self.capacitance5, self.cap_ratio5 * 100))
        sleep(.2)  # Debounce press
        return self.cap_ratio5
