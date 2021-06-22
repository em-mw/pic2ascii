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

    

    
    for zink in range(properseq):
        try:shutil.rmtree(str(os.getcwd()) + str(dirslash) + str(int(zink + 1)))
        except:os.mkdir((str(os.getcwd()) + str(dirslash) + str(int(zink + 1))))
        else:os.mkdir((str(os.getcwd()) + str(dirslash) + str(int(zink + 1))))
        
        if os.path.isdir(str(os.getcwd()) + str(dirslash) + str(int(zink +1)) + str(dirslash) + 'outputTextFiles') == bool(False):
            os.mkdir(str(os.getcwd()) + str(dirslash) + str(int(zink +1)) + str(dirslash) + 'outputTextFiles')
        if os.path.isdir(str(os.getcwd()) + str(dirslash) + str(int(zink +1)) + str(dirslash) + 'outputPictureFiles') == bool(False):
            os.mkdir(str(os.getcwd()) + str(dirslash) + str(int(zink +1)) + str(dirslash) + 'outputPictureFiles')
        if os.path.isdir(str(os.getcwd()) + str(dirslash) + str(int(zink + 1)) + str(dirslash) + 'outputTF') == bool(False):
            os.mkdir(str(os.getcwd()) + str(dirslash) + str(int(zink + 1)) + str(dirslash) + 'outputTF')
    del zink

    round = int(0)
    for thing in range(properseq):
        var = open(str(os.getcwd()) + str(dirslash) + str(int(thing + 1)) + str(dirslash) + 'var' + '.tmp', 'w')
        var.write(str('oneCharWidth = 10') + '\n' + str('oneCharHeight = 18') + '\n' + str('scaleFactor = 0.09'))
        var.close()
        tmp = open(str(os.getcwd()) + str(dirslash) + str(int(thing + 1)) + str(dirslash) + 'tmp' + '.tmp', 'w')
        tmp.write('[')
        tmp.write(str(file_path_list[int(thing)]))
        if len(file_path_list) == int(properseq):
            tmp.write(']')
        else:
            tmp.write(', ')
        try:int(int(len(file_path_list)) / int(properseq))
        except:
            modproc = math.floor(int(len(file_path_list)) / int(properseq))
            extproc = int(len(file_path_list)) // int(properseq)
            add2 = modproc
            for hallo in range(int(modproc)):
                tmp.write(str(list(file_path_list)[int(hallo + add2)]))
                add2 = add2 + properseq
            if round > modproc:
                #finnish up round and modproc right here
                round += int(1)
                pass
            del add2
        else:
            add = int(int(len(list(file_path_list))) / int(properseq))
            add -= 1
            add2 = properseq
            for hello in range(add):
                tmp.write(str(file_path_list[int(int(add2) + int(thing))]))
                add2 = add2 + properseq
                if int(hello + 1) != add:
                    tmp.write(', ')
                elif int(hello + 1) == add:
                    tmp.write(']')
            try:del hello
            except:pass
            del thing
            del add
            del add2
        tmp.close()