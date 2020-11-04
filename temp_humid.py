import board
from busio import I2C
import adafruit_bme680

class TempHumid():
  def __init__(self):
    # Create library object using our Bus I2C port
    self.i2c = I2C(board.SCL, board.SDA)
    self.bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c, debug=False)
    self.bme680.sea_level_pressure = 1013.25
    self.temperature_offset = -5

  def GetHumidity(self):
    return self.bme680.humidity

  def GetPressure(self):
    return self.bme680.pressure

  def GetAltitude(self):
    return self.bme680.altitude
