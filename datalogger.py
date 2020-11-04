import time
import air_quality
import display
import high_precis_temp
import temp_humid
import board
import busio

def main():
  # Initialize i2c bus
  i2c = busio.I2C(board.SCL, board.SDA, frequency=400000)
  # Initialize i2c devices, on bus
  oled = display.Oled(i2c, 0x3D)
  aq = air_quality.AirQuality(i2c)
  hpt = high_precis_temp.HighPrecisTemp(i2c)
  th = temp_humid.TempHumid(i2c)

  while True:
    # oled.Write(0, "T:{}F H:{} P:{}Pa".format((hpt.GetTemp()['F'], th.GetHumidity(), th.GetPressure())))
    oled.Write(0, "T:{:04.2f} F, H:{:04.2f} %".format(hpt.GetTemp()['F'], th.GetHumidity()))
    oled.Write(1, "P:{:06.2f} Pa".format(th.GetPressure()))
    time.sleep(0.1)
if __name__ == "__main__":
  main()
