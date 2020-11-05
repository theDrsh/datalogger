import board
import busio
import adafruit_pm25

class AirQuality():
  def __init__(self, i2c_bus):
    self.i2c = i2c_bus
    self.pm25 = adafruit_pm25.PM25_I2C(self.i2c, None)
  def GetData(self):
    try:
      self.aqdata = self.pm25.read()
      return self.aqdata
    except RuntimeError:
      print("Missed a sample")
      return self.aqdata
    return self.aqdata
  def GetAQI(self):
    self.GetData()
    pm2_5 = self.aqdata["particles 25um"]
    if pm2_5 <= 55:
        aqi = round(6.49*(pm2_5**0.778))
    elif 55 < pm2_5 <= 150:
        aqi = round(0.518*pm2_5+122)
    elif 150 < pm2_5:
        aqi = pm2_5+50

    if aqi <= 50:
        level = 'GOOD'
    elif 50 < aqi <= 100:
        level = 'MODERATE'
    elif 100 < aqi <= 150:
        level = 'UNHEALTHY4SOME'
    elif 150 < aqi <= 200:
        level = 'UNHEALTHY'
    elif 200 < aqi <= 300:
        level = 'VERY UNHEALTHY'
    elif 300 < aqi < 999:
        level = 'HAZARDOUS'
    else:
        level = 'SENSOR FAULT'
    return {"AQI" : aqi, "LEVEL" : level}
