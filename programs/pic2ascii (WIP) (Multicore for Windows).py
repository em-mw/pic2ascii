import math
from time import sleep
from tkinter import *
from tkinter.filedialog import askopenfilenames
#from os import getcwd
import os
import shutil


oneCharWidth = 10
oneCharHeight = 18



scaleFactor = 0.09
properseq = int(3)

def truncate_utf8_chars(filename, count, ignore_newlines=True):
    """
    Truncates last `count` characters of a text file encoded in UTF-8.
    :param filename: The path to the text file to read
    :param count: Number of UTF-8 characters to remove from the end of the file
    :param ignore_newlines: Set to true, if the newline character at the end of the file should be ignored
    """
    with open(filename, 'rb+') as f:
        last_char = None

        size = os.fstat(f.fileno()).st_size

        offset = 1
        chars = 0
        while offset <= size:
            f.seek(-offset, os.SEEK_END)
            b = ord(f.read(1))

            if ignore_newlines:
                if b == 0x0D or b == 0x0A:
                    offset += 1
                    continue

            if b & 0b10000000 == 0 or b & 0b11000000 == 0b11000000:
                # This is the first byte of a UTF8 character
                chars += 1
                if chars == count:
                    # When `count` number of characters have been found, move current position back
                    # with one byte (to include the byte just checked) and truncate the file
                    f.seek(-1, os.SEEK_CUR)
                    f.truncate()
                    return
            offset += 1

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
        except:
            try:os.mkdir((str(os.getcwd()) + str(dirslash) + str(int(zink + 1))))
            except:
                print('You have a file open or being acsessed in:\n\n' + str(os.getcwd()) + str(dirslash) + str(int(zink + 1)) + '\n\nplease close the program that is acsessing this folder and try again.')
                sleep(1)
                print('exiting')
                sleep(.3)
                exit()
        else:os.mkdir((str(os.getcwd()) + str(dirslash) + str(int(zink + 1))))
        
        if os.path.isdir(str(os.getcwd()) + str(dirslash) + str(int(zink +1)) + str(dirslash) + 'outputTextFiles') == bool(False):
            os.mkdir(str(os.getcwd()) + str(dirslash) + str(int(zink +1)) + str(dirslash) + 'outputTextFiles')
        if os.path.isdir(str(os.getcwd()) + str(dirslash) + str(int(zink +1)) + str(dirslash) + 'outputPictureFiles') == bool(False):
            os.mkdir(str(os.getcwd()) + str(dirslash) + str(int(zink +1)) + str(dirslash) + 'outputPictureFiles')
        if os.path.isdir(str(os.getcwd()) + str(dirslash) + str(int(zink + 1)) + str(dirslash) + 'outputTF') == bool(False):
            os.mkdir(str(os.getcwd()) + str(dirslash) + str(int(zink + 1)) + str(dirslash) + 'outputTF')
    del zink

    round = int(0)
    extitems = {}
    for tmp in range(len(list(file_path_list))):
        extitems[tmp] = False
    del tmp

    for thing in range(properseq):
        var = open(str(os.getcwd()) + str(dirslash) + str(int(thing + 1)) + str(dirslash) + 'var' + '.tmp', 'w')
        var.write(str('oneCharWidth = 10') + '\n' + str('oneCharHeight = 18') + '\n' + str('scaleFactor = 0.09'))
        var.close()
        tmp = open(str(os.getcwd()) + str(dirslash) + str(int(thing + 1)) + str(dirslash) + 'tmp' + '.tmp', 'w')
        tmp.write('[')
        tmp.write(str(file_path_list[int(thing)]))
        extitems[thing] = True
        if len(file_path_list) == int(properseq):
            tmp.write(']')
        else:
            tmp.write(', ')
            if isinstance(int(len(file_path_list)) / int(properseq), float):
                evenproc = int(math.floor(int(int(len(list(file_path_list))) / int(properseq))))
                extraproc = int(int(len(list(file_path_list))) // int(properseq))
                add2 = properseq
                for hello in range(int(evenproc - 1)):
                    tmp.write(str(list(file_path_list)[int(int(add2) + int(thing))]))
                    extitems[int(int(add2) + int(thing))] = True
                    add2 = add2 + properseq
                    if int(hello + 1) != int(evenproc - 1):
                        tmp.write(', ')
                    elif int(hello + 1) == int(evenproc - 1):
                        tmp.write(']')
            if isinstance(int(len(file_path_list)) / int(properseq), int):
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
            #shutil.copy(str(str(os.getcwd() + str(dirslash) + 'gen-files' + str(dirslash) + 'start.engine.cmd')), str(os.getcwd() + str(dirslash) + str(int(thing + 1)))
        tmp.close()
    if isinstance(int(len(file_path_list)) / int(properseq), float):
        truncate_utf8_chars(os.getcwd() + str(dirslash) + '1' + str(dirslash) + 'tmp.tmp', 1)
        with open(os.getcwd() + str(dirslash) + '1' + str(dirslash) + 'tmp.tmp', 'a') as tmpaft:
            tmpaft.write(', ')
            for lol in range(len(extitems)):
                if extitems[lol]:
                    del extitems[lol]
            del lol
            extitems = list(extitems.keys())
            for keytorun in range(len(extitems)):
                tmpaft.write(str(list(file_path_list)[extitems[keytorun]]))
            tmpaft.write(']')
    input('done! (press enter to exit)')
