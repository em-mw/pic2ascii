import PIL
from PIL import ImageDraw, ImageFont
from tqdm import tqdm
import math
from tkinter.filedialog import askopenfilenames
from tkinter import *
from time import sleep
chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]
charArray = list(chars)
charLength = len(charArray)
interval = charLength/256

oneCharWidth = 10
oneCharHeight = 18

def getChar(inputInt):
    return charArray[math.floor(inputInt*interval)]

sf = input('Hello Enter Scale Factor or \'d\' for the default scale factor')
if 'd' in sf:
    scaleFactor = .05
else:
    try:
        int(sf)
    except:
        print('this does not work')
        sleep(.2)
        print('exiting')
        sleep(.5)
        exit()
    else:
        sf = scaleFactor
        sf = _
print('select image or image sequance.')
sleep(.5)
fileman = Tk()
fileman.wm_state('iconic')
file_path_list = askopenfilenames(filetypes=(("JPEG/JPG files","*.jpeg *.jpg"), ("Any file", "*")), initialdir="/", title='Select pictures.')
file_path_list = list(file_path_list)

back = str(chr(92))
x = 0
for file in file_path_list:
        
    im = PIL.Image.open(file_path_list[x])
        

    fnt = ImageFont.truetype('C:\\Windows\\Fonts\\lucon.ttf', 15)

    width, height = im.size
    im = im.resize((int(scaleFactor*width), int(scaleFactor*height*(oneCharWidth/oneCharHeight))), PIL.Image.NEAREST)
    width, height = im.size
    pix = im.load()

    outputImage = PIL.Image.new('RGB', (oneCharWidth * width, oneCharHeight * height), color = (0, 0, 0))
    d = ImageDraw.Draw(outputImage)

    for i in tqdm(range(height)):
        for j in range(width):
            r, g, b = pix[j, i]
            h = int(r/3 + g/3 + b/3)
            pix[j, i] = (h, h, h)
            d.text((j*oneCharWidth, i*oneCharHeight), getChar(h), font = fnt, fill = (r, g, b))
        
    r = file_path_list[x].replace('/', back)
    x += 1
    if x < 10:
        outputImage.save(r.replace('.jpg', '.png'))
    elif x < 100:
        outputImage.save(r.replace('.jpg', '.png'))
    elif x < 1000:
        outputImage.save(r.replace('.jpg', '.png'))
    else:
        outputImage.save(r.replace('.jpg', '.png'))

input('done(enter to exit)')
