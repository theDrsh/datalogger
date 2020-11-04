import board
import busio
import adafruit_pm25

class AirQuality():
  def __init__(self, i2c_bus):
    self.i2c = i2c_bus
    self.pm25 = adafruit_pm25.PM25_I2C(self.i2c, None)
  def GetData(self):
    self.aqdata = self.pm25.read()
    return self.aqdata
