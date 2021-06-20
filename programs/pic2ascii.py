import math
from time import sleep
from tkinter import *
from tkinter.filedialog import askopenfilenames
from os import getcwd
import os
import shutil


oneCharWidth = 10
oneCharHeight = 18



scaleFactor = 0.09
properseq = int(3)


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
    if str(os.name) == 'nt':
        dirslash = '\\'
    else:
        dirslash = '/'
    
    print('starting...', end='\n\n')

    
    if os.path.isdir(str(os.getcwd()) + str(dirslash) + 'outputTextFiles') == bool(False):
        os.mkdir(str(os.getcwd()) + str(dirslash) + 'outputTextFiles')
    if os.path.isdir(str(os.getcwd()) + str(dirslash) + 'outputPictureFiles') == bool(False):
        os.mkdir(str(os.getcwd()) + str(dirslash) + 'outputPictureFiles')
    if os.path.isdir(str(os.getcwd()) + str(dirslash) + 'outputTF') == bool(False):
        os.mkdir(str(os.getcwd()) + str(dirslash) + 'outputTF')
    
    for zink in range(properseq):
        try:shutil.rmtree(str(os.getcwd()) + str(dirslash) + 'outputPictureFiles' + str(dirslash) + str(int(zink + 1)))
        except:os.mkdir((str(os.getcwd()) + str(dirslash) + 'outputPictureFiles' + str(dirslash) + str(int(zink + 1))))
        else:os.mkdir((str(os.getcwd()) + str(dirslash) + 'outputPictureFiles' + str(dirslash) + str(int(zink + 1))))
    del zink

    for thing in range(properseq):
        var = open(str(os.getcwd()) + str(dirslash) + 'outputPictureFiles' + str(dirslash) + str(int(thing + 1)) + str(dirslash) + 'var' + '.tmp', 'w')
        var.write(str(oneCharWidth = 10) + ' ' + str(oneCharHeight = 18) + ' ' + str(scaleFactor = 0.09))
        var.close()
        tmp = open(str(os.getcwd()) + str(dirslash) + 'outputPictureFiles' + str(dirslash) + str(int(thing + 1)) + str(dirslash) + 'tmp' + '.tmp', 'w')
        tmp.write('[')
        tmp.write(str(file_path_list[int(thing)]) + ', ')
        try:int(int(len(file_path_list)) / int(properseq))
        except:pass
        else:
            add = int(int(len(list(file_path_list))) / int(properseq))
            add -= 1
            add2 = properseq
            for omla in range(add):
                tmp.write(str(file_path_list[int(int(add2) + int(thing))]))
                add2 = add2 + properseq
                if int(omla + 1) != add:
                    tmp.write(', ')
                else:
                    tmp.write(']')
        
        tmp.close()
    del thing
    del omla
    del add
