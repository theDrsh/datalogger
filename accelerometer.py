import board
import busio
import adafruit_bno055

class Accelerometer():
    def __init__(self, i2c_bus):
        self.i2c = i2c_bus
        self.sensor = adafruit_bno055.BNO055_I2C(self.i2c)
