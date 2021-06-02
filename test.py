import PIL
from PIL import ImageDraw, ImageFont
import os

outputImage = PIL.Image.new('RGBA', (1920, 1080), color = (0, 0, 0, 0))
d = ImageDraw.Draw(outputImage)
d.text((960, 540), 'h', fill = (255, 255, 255), font = ImageFont.truetype('C:\\Windows\\Fonts\\lucon.ttf', 15))
outputImage.save(str(os.getcwd() + '\\a.png'))