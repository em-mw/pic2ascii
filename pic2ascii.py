import PIL
from PIL import ImageDraw, ImageFont
from tqdm import tqdm
import math
from tkinter.filedialog import askopenfilenames
from tkinter import *
chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]
# chars = "#Wo- "[::-1]
charArray = list(chars)
charLength = len(charArray)
interval = charLength/256

scaleFactor = .08

oneCharWidth = 10
oneCharHeight = 18

def getChar(inputInt):
    return charArray[math.floor(inputInt*interval)]

#text_file = open("Output.txt", "w")
y_or_n = str(input('Hi, do you want to convert many pictures? (y) or (n)?'))

if y_or_n == 'y':
    fileman = Tk()
    fileman.wm_state('iconic')
    file_path_list = askopenfilenames(filetypes=(("JPEG/JPG files","*.jpeg *.jpg"), ("Any file", "*")), initialdir="/", title='Select pictures.')
    file_path_list = list(file_path_list)

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
                #text_file.write(getChar(h))
                d.text((j*oneCharWidth, i*oneCharHeight), getChar(h), font = fnt, fill = (r, g, b))
        
        x += 1
        #text_file.write('\n')
        if x < 10:
            outputImage.save('000' + str(x) + '.png')
        elif x < 100:
            outputImage.save('00' + str(x) + '.png')
        elif x < 1000:
            outputImage.save('0' + str(x) + '.png')
        else:
            outputImage.save(str(x) + '.png')
        

else:
    filename = int(input('Enter the filename of the picture. This value must be a number. Make sure to have your pic in .jpg format.'))
    im = Image.open(filename)

    fnt = ImageFont.truetype('C:\\Windows\\Fonts\\lucon.ttf', 15)

    width, height = im.size
    im = im.resize((int(scaleFactor*width), int(scaleFactor*height*(oneCharWidth/oneCharHeight))), Image.NEAREST)
    width, height = im.size
    pix = im.load()

    outputImage = Image.new('RGB', (oneCharWidth * width, oneCharHeight * height), color = (0, 0, 0))
    d = ImageDraw.Draw(outputImage)

    for i in tqdm(range(height)):
        for j in range(width):
            r, g, b = pix[j, i]
            h = int(r/3 + g/3 + b/3)
            pix[j, i] = (h, h, h)
            #text_file.write(getChar(h))
            d.text((j*oneCharWidth, i*oneCharHeight), getChar(h), font = fnt, fill = (r, g, b))

    #text_file.write('\n')

    outputImage.save(filename +'ascii')
