# How to - Scan local WLAN
import network
import esp

class WLANscan:

    def __init__(self):

        esp.osdebug(None)
        self.wlan = network.WLAN(network.STA_IF)

    def ssid(self):

        netlist=[]

        self.wlan.active(True)

        xnet = self.wlan.scan()

        self.wlan.active(False)

        for ynet in xnet:
            znet = str(ynet[0])
            netlist.append(znet[2:len(znet)-1])

        return netlist


    def channel(self):

        netlist=[]

        self.wlan.active(True)

        xnet = self.wlan.scan()

        self.wlan.active(False)

        for ynet in xnet:
            netlist.append(str(ynet[2]))

        return netlist

    def rssi(self):

        netlist=[]

        self.wlan.active(True)

        xnet = self.wlan.scan()

        self.wlan.active(False)

        for ynet in xnet:
            netlist.append(str(ynet[3]))

        return netlist


    def authmode(self):

        netlist=[]

        self.wlan.active(True)

        xnet = self.wlan.scan()

        self.wlan.active(False)

        for ynet in xnet:
            netlist.append(str(ynet[4]))

        return netlist


    def hidden(self):

        netlist=[]

        self.wlan.active(True)

        xnet = self.wlan.scan()

        self.wlan.active(False)

        for ynet in xnet:
            netlist.append(str(ynet[5]))

        return netlist


def main():
    test = WLANscan()
    print(str(test.hidden()))


if __name__ == '__main__':
    main()
