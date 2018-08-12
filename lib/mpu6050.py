import machine


class accel():
    def __init__(self, i2c, addr):  #addr=0x68
        self.iic = i2c
        self.addr = addr
        self.iic.start()
        self.iic.writeto(self.addr, bytearray([107, 0]))
        self.iic.writeto_mem(self.addr, 0x1C, b'\x00\x00\x00\x01\x01\x00\x00\x00')
        self.iic.stop()

    def set_frs_ac(self, scale):
        if scale == 0:
            self.iic.writeto_mem(self.addr, 0x1C, b'\x00\x00\x00\x00\x00\x00\x00\x00')
        if scale == 1:
            self.iic.writeto_mem(self.addr, 0x1C, b'\x00\x00\x00\x00\x01\x00\x00\x00')
        if scale == 2:
            self.iic.writeto_mem(self.addr, 0x1C, b'\x00\x00\x00\x01\x00\x00\x00\x00')
        if scale == 3:
            self.iic.writeto_mem(self.addr, 0x1C, b'\x00\x00\x00\x01\x01\x00\x00\x00')

    def set_frs_gy(self, scale):
        if scale == 0:
            self.iic.writeto_mem(self.addr, 0x1B, b'\x00\x00\x00\x00\x00\x00\x00\x00')
        if scale == 1:
            self.iic.writeto_mem(self.addr, 0x1B, b'\x00\x00\x00\x00\x01\x00\x00\x00')
        if scale == 2:
            self.iic.writeto_mem(self.addr, 0x1B, b'\x00\x00\x00\x01\x00\x00\x00\x00')
        if scale == 3:
            self.iic.writeto_mem(self.addr, 0x1B, b'\x00\x00\x00\x01\x01\x00\x00\x00')

    def get_raw_values(self):
        self.iic.start()
        a = self.iic.readfrom_mem(self.addr, 0x3B, 14)
        self.iic.stop()
        return a

    def read_scale(self, regaddr):
        self.regaddr = int(hex(regaddr))
        self.iic.start()
        s = self.iic.readfrom_mem(self.addr,self.regaddr, 8)
        self.iic.stop()
        return s

    def get_ints(self):
        b = self.get_raw_values()
        c = []
        for i in b:
            c.append(i)
        return c

    def bytes_toint(self, firstbyte, secondbyte):
        if not firstbyte & 0x80:
            return firstbyte << 8 | secondbyte
        return - (((firstbyte ^ 255) << 8) | (secondbyte ^ 255) + 1)

    def get_values(self):
        raw_ints = self.get_raw_values()
        vals = {}
        vals["AcX"] = self.bytes_toint(raw_ints[0], raw_ints[1])
        vals["AcY"] = self.bytes_toint(raw_ints[2], raw_ints[3])
        vals["AcZ"] = self.bytes_toint(raw_ints[4], raw_ints[5])
        vals["Tmp"] = self.bytes_toint(raw_ints[6], raw_ints[7]) / 340.00 + 36.53
        vals["GyX"] = self.bytes_toint(raw_ints[8], raw_ints[9])
        vals["GyY"] = self.bytes_toint(raw_ints[10], raw_ints[11])
        vals["GyZ"] = self.bytes_toint(raw_ints[12], raw_ints[13])
        return vals  # returned in range of Int16
        # -32768 to 32767

    def val_test(self):  # ONLY FOR TESTING! Also, fast reading sometimes crashes IIC
        from time import sleep
        while 1:
            print(self.get_values())
            sleep(0.05)
