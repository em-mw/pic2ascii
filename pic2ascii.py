import PIL
from PIL import ImageDraw, ImageFont
from tqdm import tqdm
import math
from tkinter.filedialog import askopenfilenames
from tkinter import *
from time import sleep
from multiprocessing import Process

chars = '''$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. '''[::-1]
charArray = list(chars)
charLength = len(charArray)
interval = charLength/256

oneCharWidth = 10
oneCharHeight = 18

class start:
    def getChar(self, inputInt):
        return charArray[math.floor(inputInt*interval)]

    def main(self):
        scaleFactor = input('Hello Enter Scale Factor')
        try:
            int(scaleFactor)
        except:
            print('this does not work')
            sleep(.2)
            print('making default')
            sleep(.5)
            scaleFactor = 0.4
        print('select image or image sequance.')
        sleep(.5)
        print('opening window')
        sleep(.2)
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

            outputImage = PIL.Image.new('RGB', (oneCharWidth * width, oneCharHeight * height), color = (64, 64, 64))
            #outputImage = im
            d = ImageDraw.Draw(outputImage)

            for i in tqdm(range(height)):
                for j in range(width):
                    r, g, b = pix[j, i]
                    h = int(r/3 + g/3 + b/3)
                    pix[j, i] = (h, h, h)
                    d.text((j*oneCharWidth, i*oneCharHeight), p.getChar(h), font = fnt, fill = (r, g, b))
                
            r = file_path_list[x].replace('/', '\\')
            x += 1
            outputImage.save(r.replace('.jpg', '.png'))
#for class
p = start()

# if __name__ == '__main__':
    # p1 = Process(target=p.main)
    # input('yes')
    # p1.start()

    # p1.join()
    # input('done(enter to exit)')

p.main()
