import pystray
from PIL import Image, ImageDraw, ImageFont

class SysTray():

	def __init__(self):
		self.icon = pystray.Icon('')

		self.img  = Image.new('RGBA', (32, 32))
		self.draw = ImageDraw.Draw(self.img)
		self.font = ImageFont.truetype("bld.ttf", 27)

	def setTrayNumber(self,digit):

		self.img  = Image.new('RGBA', (32, 32))
		self.draw = ImageDraw.Draw(self.img)

		self.draw.text((1, -4), digit, (255, 255, 255, 255),font=self.font)
		self.img.save('sample-out.png')

		self.icon.icon = self.img