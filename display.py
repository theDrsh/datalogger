import board
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

class Oled():
  def __init__(self, i2c_bus, address):
    self.height = 32
    self.width = 128
    self.i2c = i2c_bus
    self.oled = adafruit_ssd1306.SSD1306_I2C(self.width, self.height, self.i2c, addr=address)
    self.font = ImageFont.load_default()
    self.text = ["", "", ""]

  def Clear(self):
    self.oled.fill(0)
    self.oled.show()
    self.image = Image.new("1", (self.oled.width, self.oled.height))

  def Write(self, line_num, text):
    image = Image.new("1", (self.oled.width, self.oled.height))
    draw = ImageDraw.Draw(image)
    font_height = self.font.getsize(text)[-1]
    draw.text( (0, font_height * line_num), text, font=self.font, fill=255)
    if len(text) >= 20:
      print("String too long: %s"%(text))
    elif (line_num > 2) or (line_num < 0):
      print("Line num must be > 0 and < 3 it is: %d"%(line_num))
    else:
      self.text[line_num] = text
      self.oled.image(image)
      self.oled.show()
