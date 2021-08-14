import math
from time import sleep
from tkinter import *
from tkinter.filedialog import askopenfilenames
#from os import getcwd
import os
import shutil
def lols():


    oneCharWidth = 10
    oneCharHeight = 18



    scaleFactor = 0.09
    properseq = int(3)

    def isInt(num):
        """
        Finds if a number is an int or a float.
        This is a better version of the "isinstance"
        function in python. This function returns a
        bool value (like the "isinstance" function)
        :param num: The number to check if is a int
        ::returns True if int
        ::returns False if float
        """
        if str(type(num)) == '<class \'int\'>' or str(type(num)) == '<class \'float\'>':
            num = str(num)
            if num.find('.'):
                if len(num) >= 3:
                    if num[2].find('0') == int(-1):
                        return False
                    else:
                        return True
                else:
                    return True
            else:
                return True
        else:
            return None

    def isFloat(num):
        """
        Finds if a number is an int or a float.
        This is a better version of the "isinstance"
        function in python. This function returns a
        bool value (like the "isinstance" function)
        :param num: The number to check if is a float
        ::returns False if int
        ::returns True if float
        """
        if str(type(num)) == '<class \'int\'>' or str(type(num)) == '<class \'float\'>':
            num = str(num)
            if num.find('.'):
                if len(num) >= 3:
                    if num[2].find('0') == int(-1):
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return None


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
            
            # if os.path.isdir(str(os.getcwd()) + str(dirslash) + str(int(zink +1)) + str(dirslash) + 'outputTextFiles') == bool(False):
            #     os.mkdir(str(os.getcwd()) + str(dirslash) + str(int(zink +1)) + str(dirslash) + 'outputTextFiles')
            # if os.path.isdir(str(os.getcwd()) + str(dirslash) + str(int(zink +1)) + str(dirslash) + 'outputPictureFiles') == bool(False):
            #     os.mkdir(str(os.getcwd()) + str(dirslash) + str(int(zink +1)) + str(dirslash) + 'outputPictureFiles')
            # if os.path.isdir(str(os.getcwd()) + str(dirslash) + str(int(zink + 1)) + str(dirslash) + 'outputTF') == bool(False):
            #     os.mkdir(str(os.getcwd()) + str(dirslash) + str(int(zink + 1)) + str(dirslash) + 'outputTF')
        del zink

        extitems = {}
        for tmp in range(len(list(file_path_list))):
            extitems[tmp] = False
        del tmp

        for thing in range(properseq):
            tmp = open(str(os.getcwd()) + str(dirslash) + str(int(thing + 1)) + str(dirslash) + 'tmp' + '.tmp', 'w')
            tmp.write('[')
            for in_file in range(math.floor(int(len(file_path_list)) / int(properseq))):
                tmp.write(str(file_path_list[int(thing)]))
                extitems[thing] = True
                if int(in_file + 1) == math.floor(int(len(file_path_list)) / int(properseq)):pass
                else:tmp.write(', ')
            if int(thing + 1) == int(properseq) and isFloat(int(len(file_path_list)) / int(properseq)):
                tmp.write(', ')
                extitems2 = extitems.copy()
                for delif in extitems2:
                    if extitems[delif] == True:
                        del extitems[delif]
                del extitems2
                tls=0
                extlist = list(extitems.keys())
                for witems in extlist:
                    tmp.write(str(list(file_path_list)[int(witems)]))
                    tls += 1
                    if int(len(extlist)) == int(tls):pass
                    else:tmp.write(', ')
                    
            tmp.write(']')
            tmp.close()
        input('done! press enter to exit')
lols()