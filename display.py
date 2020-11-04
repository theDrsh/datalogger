import board
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

class Oled():
  def __init__(self, i2c_bus, address):
    self.height = 64
    self.width = 128
    self.i2c = i2c_bus
    self.oled = adafruit_ssd1306.SSD1306_I2C(self.width, self.height, self.i2c, addr=address)
    self.font = ImageFont.load_default()
    font_height = self.font.getsize("TEST")[-1]
    # Create text storage for number of lines that fit in oled size
    self.text = []
    for i in range(round(self.oled.height/(font_height))):
      self.text.insert(i, "")

  def Clear(self):
    self.oled.fill(0)
    self.oled.show()
    self.image = Image.new("1", (self.oled.width, self.oled.height))

  def Write(self, line_num, text):
    image = Image.new("1", (self.oled.width, self.oled.height))
    draw = ImageDraw.Draw(image)
    (font_width, font_height) = self.font.getsize(text)
    char_size = font_width // len(text)
    chars_avail = self.oled.width // char_size
    if font_width > self.oled.width:
      print("String too long: %s, %d > %d"%(text, len(text), chars_avail))
    elif line_num > len(self.text) - 1:
      print("Too many lines, %d > %d"%(line_num, len(self.text) - 1))
    else:
      i = 0
      for line in self.text:
        draw.text((0, (font_height/2) * i), line, font=self.font, fill=255)
        i+=2
      self.text[line_num] = text
      self.oled.image(image)
      self.oled.show()
