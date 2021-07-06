import PIL
from PIL import ImageDraw, ImageFont
from sty import fg
import math
from time import sleep
from os import getcwd
import os
import shutil

def getChar(self, inputInt):
    chars = '''$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. '''[::-1]
    charArray = list(chars)
    charLength = len(charArray)
    interval = charLength/256
    
    return charArray[math.floor(inputInt*interval)]

os.system("")

if str(os.name) == 'nt':
    dirslash = '\\'
else:
    dirslash = '/'
chars = '''$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. '''[::-1]

charArray = list(chars)
charLength = len(charArray)
interval = charLength/256

with open('var.tmp', 'r') as var:
    exec(var.read())
del var
with open('tmp.tmp', 'r') as tmp:
    file_path_list = tmp.read().splitlines()[int(0)]
del tmp

x = 0
for file in file_path_list:
    
    im = PIL.Image.open(file_path_list[int(x)])
    if file_path_list[int(x)][-4] == '.' and file_path_list[int(x)][-3] == 'p' and file_path_list[int(x)][-2] == 'n' and file_path_list[int(x)][-1] == 'g':
        format = 'RGBA'
    else:
        format = 'RGB'
    fnt = ImageFont.truetype('C:\\Windows\\Fonts\\lucon.ttf', 15)

    width, height = im.size
    im = im.resize((int(scaleFactor*width), int(scaleFactor*height*(oneCharWidth/oneCharHeight))), PIL.Image.NEAREST)
    width, height = im.size
    pix = im.convert(str(format))

    outputImage = PIL.Image.new(str(format), (oneCharWidth * width, oneCharHeight * height), color = (0, 0, 0))

    d = ImageDraw.Draw(outputImage)
    

    
    tf = open(str(os.getcwd()) + str(dirslash) + 'outputTF' + str(dirslash) + str(int(x + 1)) + '.txt', "w")
    text_file = open(str(os.getcwd()) + str(dirslash) + 'outputTextFiles' + str(dirslash) + str(f"Output{int(x) + int(1)}.txt"), "w")
    for i in range(height):
        for j in range(width):
            if format == 'RGBA':
                r, g, b, a = pix.getpixel((j, i))
            elif format == 'RGB':
                r, g, b = pix.getpixel((j, i))
            #r, g, b = pix[j, i]
            h = int(r/3 + g/3 + b/3)
            #pix.getpixel((j, i)) = (h, h, h)#line no work nomore
            text_file.write(getChar(h))
            tf.write(str(fg(r, g, b)) + str(getChar(h)))
            if format == 'RGBA':
                d.text((math.ceil(int(j*oneCharWidth)), math.ceil(int(i*oneCharHeight))), getChar(h), font = fnt, fill = (int(r), int(g), int(b), int(a)))
            elif format == 'RGB':
                d.text((math.ceil(int(j*oneCharWidth)), math.ceil(int(i*oneCharHeight))), getChar(h), font = fnt, fill = (int(r), int(g), int(b)))
            try:
                print(fg(r, g, b) + str(getChar(h)), end='') #please don't put fg.rs into the code or it will slow down a lot
            except:
                try:
                    print(str(getChar(h)), end='')
                except:
                    print('?', end='')
        tf.write('\n')
        text_file.write('\n')
        print()
    text_file.close()
    tf.close()
    x += int(1)
    outputImage.save(str(os.getcwd()) + str(dirslash) + 'outputPictureFiles' + str(dirslash) + 'output' + str(x) + '.png')
    if int(len(file_path_list)) >= int(x + 1):
        print(f'{fg.rs}\n\nImage {x} is done, going to next image\n\n')

    try:input(fg.rs + '\n\nall done! Press enter to exit!')
    except:input('\n\nall done! Press enter to exit!')