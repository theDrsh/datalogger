import time
import board
import busio
import adafruit_mcp9808

class HighPrecisTemp():
  def __init__(self, i2c_bus):
    self.i2c = i2c_bus
    self.mcp = adafruit_mcp9808.MCP9808(self.i2c)
  def GetTemp(self):
    self.tempC = self.mcp.temperature
    self.tempF = self.tempC * 9 / 5 + 32
    return {"C": self.tempC, "F" : self.tempF}
