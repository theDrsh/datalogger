import board
import busio
import adafruit_pm25

class AirQuality():
  def __init__(self):
    self.i2c = busio.I2C(board.SCL, board.SDA)
    self.pm25 = adafruit_pm25.PM25_I2C(self.i2c, None)
  def GetData(self):
    self.aqdata = self.pm25.read()
    return self.aqdata
