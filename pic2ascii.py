from PIL import Image, ImageDraw, ImageFont
from tqdm import tqdm
import math

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
y_or_n = str(input('Hi, do tou want to convert many pictures? (y) or (n)?'))

if y_or_n == 'y':
    howmany = int(input('How many pictures do you have? This must have a number value.'))
    filename = int(input('Enter the filename of the first picture. This must also be a number. Also make sure to have your pics in .jpg format.'))
    while filename < howmany:
        filename = filename + 1
        if filename < 10:
            im = Image.open('000' + str(filename) + '.jpg')
        elif filename < 100:
            im = Image.open('00' + str(filename) + '.jpg')
        elif filename < 1000:
            im = Image.open('0' + str(filename) + '.jpg')
        else:
            im = Image.open(filename + '.jpg')
            
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

        if filename < 10:
            outputImage.save('output' + '000' + str(filename) + '.png')
        elif filename < 100:
            outputImage.save('output' + '00' + str(filename) + '.png')
        elif filename < 1000:
            outputImage.save('output' + '0' + str(filename) + '.png')
        else:
            outputImage.save(str(filename) + '.png')



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

    outputImage.save('output.png')

