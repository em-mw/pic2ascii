import math
from multiprocessing import Process
from time import sleep
from tkinter import *
from tkinter.filedialog import askopenfilenames
from os import getcwd
import os

import PIL
from PIL import ImageDraw, ImageFont

#if you want the normal loading screen you have to uncomment the import and add the function to the first for loop like this [for i in tqdm(range(height)):]
#from tqdm import tqdm

chars = '''$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. '''[::-1]
charArray = list(chars)
charLength = len(charArray)
interval = charLength/256


class start:
    def getChar(self, inputInt):
        return charArray[math.floor(inputInt*interval)]
    
    def main(self):
        oneCharWidth = 10
        oneCharHeight = 18
        
        
        scaleFactor = 0.03

        fileman = Tk()
        fileman.wm_state('iconic')
        file_path_list = askopenfilenames(filetypes=(("JPEG/JPG files","*.jpeg *.jpg"), ("Any file", "*")), initialdir="/", title='Select pictures.')
        #fileman.mainloop()
        file_path_list = list(file_path_list)
        if not file_path_list:
            print('you have no files selected')
            sleep(1)
            exit()
        else:
            #this variable (x) is a preuse of the while loop. We will keep this variable for future purposes
            x = 0
            if str(os.name) == 'nt':
                dirslash = '\\'
            else:
                dirslash = '/'
            
            print('starting...', end='\n\n')
            for file in file_path_list:
                
                im = PIL.Image.open(file_path_list[int(x)])

                fnt = ImageFont.truetype('C:\\Windows\\Fonts\\lucon.ttf', 15)

                width, height = im.size
                im = im.resize((int(scaleFactor*width), int(scaleFactor*height*(oneCharWidth/oneCharHeight))), PIL.Image.NEAREST)
                width, height = im.size
                pix = im.load()

                outputImage = PIL.Image.new('RGB', (oneCharWidth * width, oneCharHeight * height), color = (0, 0, 0))
                d = ImageDraw.Draw(outputImage)
                
                if os.path.isdir(str(os.getcwd()) + str(dirslash) + 'TextFiles') == bool(False):
                    os.mkdir(str(os.getcwd()) + str(dirslash) + 'TextFiles')
                if os.path.isdir(str(os.getcwd()) + str(dirslash) + 'PictureFiles') == bool(False):
                    os.mkdir(str(os.getcwd()) + str(dirslash) + 'PictureFiles')

                text_file = open(str(os.getcwd()) + str(dirslash) + 'TextFiles' + str(dirslash) + str(f"Output{int(x) + int(1)}.txt"), "w")
                for i in range(height):
                    for j in range(width):
                        r, g, b = pix[j, i]
                        h = int(r/3 + g/3 + b/3)
                        pix[j, i] = (h, h, h)
                        text_file.write(self.getChar(h))
                        d.text((j*oneCharWidth, i*oneCharHeight), self.getChar(h), font = fnt, fill = (r, g, b))
                        print(charArray[math.floor(h*interval)], end='')
                    x += int(1)
                    outputImage.save(str(os.getcwd()) + str(dirslash) + 'PictureFiles' + str(dirslash) + 'output' + str(x) + '.png')
                    text_file.write('\n')
                    print()
                text_file.close()
                if int(len(file_path_list)) >= int(x):
                    print(f'\n\nImage {x} is done, going to next image\n\n')
                
#for class
p = start()

# if __name__ == '__main__':
    # p1 = Process(target=p.main)
    # input('yes')
    # p1.start()

    # p1.join()
    # input('done(enter to exit)')

p.main()
input('\n\nall done! Press enter to exit!')
