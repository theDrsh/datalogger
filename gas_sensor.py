import time
import board
import busio
import adafruit_ccs811

class GasSensor():
    def __init__(self, i2c_bus):
        self.i2c = i2c_bus
        self.ccs811 = adafruit_ccs811.CCS811(self.i2c)
        self.data = {"ECO2" : int(0), "TVOC": int(0)}
    def GetData(self):
        if self.ccs811.data_ready:
            self.data["ECO2"] = self.ccs811.eco2
            self.data["TVOC"] = self.ccs811.tvoc
        return self.data
