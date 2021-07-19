import math
#from multiprocessing import Process
from time import sleep
from tkinter import *
from tkinter.filedialog import askopenfilenames
from os import getcwd
import os
from sty import fg

import PIL
from PIL import ImageDraw, ImageFont

#if you want the normal loading screen you have to uncomment the import and add the function to the first for loop like this [for i in tqdm(range(height)):]
#from tqdm import tqdm
os.system("")

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
        
        #tfFPS = int(30)
        
        scaleFactor = 0.09

        fileman = Tk()
        fileman.wm_state('iconic')
        file_path_list = askopenfilenames(filetypes=(("JPEG/JPG files","*.jpeg *.jpg"), ("PNG files (in beta)", "*.png"), ("Any file", "*")), title='Select pictures.')  #initialdir="/"
        #fileman.mainloop()
        file_path_list = list(file_path_list)
        if not file_path_list:
            print('you have no files selected')
            sleep(.5)
            print('exiting')
            sleep(.2)
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
                
                if os.path.isdir(str(os.getcwd()) + str(dirslash) + 'outputTextFiles') == bool(False):
                    os.mkdir(str(os.getcwd()) + str(dirslash) + 'outputTextFiles')
                if os.path.isdir(str(os.getcwd()) + str(dirslash) + 'outputPictureFiles') == bool(False):
                    os.mkdir(str(os.getcwd()) + str(dirslash) + 'outputPictureFiles')
                if os.path.isdir(str(os.getcwd()) + str(dirslash) + 'outputTF') == bool(False):
                    os.mkdir(str(os.getcwd()) + str(dirslash) + 'outputTF')

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
                        text_file.write(self.getChar(h))
                        tf.write(str(fg(r, g, b)) + str(self.getChar(h)))
                        if format == 'RGBA':
                            d.text((math.ceil(int(j*oneCharWidth)), math.ceil(int(i*oneCharHeight))), self.getChar(h), font = fnt, fill = (int(r), int(g), int(b), int(a)))
                        elif format == 'RGB':
                            d.text((math.ceil(int(j*oneCharWidth)), math.ceil(int(i*oneCharHeight))), self.getChar(h), font = fnt, fill = (int(r), int(g), int(b)))
                        try:
                            print(fg(r, g, b) + str(self.getChar(h)), end='') #please don't put fg.rs into the code or it will slow down a lot
                        except:
                            try:
                                print(str(self.getChar(h)), end='')
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
                
#for class
p = start()

# if __name__ == '__main__':
    # p1 = Process(target=p.main)
    # input('yes')
    # p1.start()

    # p1.join()
    # input('done(enter to exit)')

p.main()
try:input(fg.rs + '\n\nall done! Press enter to exit!')
except:input('\n\nall done! Press enter to exit!')
