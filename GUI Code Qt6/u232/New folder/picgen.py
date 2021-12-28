import math
from time import sleep
from tkinter import *
from tkinter.filedialog import askopenfilenames
#from os import getcwd
import os
import shutil


def lols(file_path_list, properseq):


#vars:
    #properseq = int(3)
###########################




    def isInt(num):
        if str(type(num)) == '<class \'int\'>' or str(type(num)) == '<class \'float\'>':
            num = str(num)
            if num.find('.') != int(-1):
                if len(num) >= 2:
                    numl = list(num)
                    elx = 0
                    dolto = int(num.find('.'))
                    for qot in numl[:]:
                        if qot.find('.') != int(-1) or int(elx) < int(dolto):
                            elx += 1
                            continue
                        elif int(elx) > int(dolto):
                            if qot.find('0') == int(-1):
                                return False
                        if str(num[-1]) == str(qot) and qot.find('0') != int(-1):
                            return True
                        elx += 1
                else:
                    return True
            else:
                return True
        else:
            return False



    def isFloat(num):
        if str(type(num)) == '<class \'int\'>' or str(type(num)) == '<class \'float\'>':
            num = str(num)
            if num.find('.') != int(-1):
                if len(num) >= 2:
                    numl = list(num)
                    elx = 0
                    dolto = int(num.find('.'))
                    for qot in numl[:]:
                        if qot.find('.') != int(-1) or int(elx) < int(dolto):
                            elx += 1
                            continue
                        elif int(elx) > int(dolto):
                            if qot.find('0') == int(-1):
                                return True
                        if str(num[-1]) == str(qot) and qot.find('0') != int(-1):
                            return False
                        elx += 1
                else:
                    return False
            else:
                return False
        else:
            return False


        
    print('starting...', end='\n\n')
    
    if os.path.isdir(str(os.getcwd()) + str(os.sep) + 'pic2asciitemp'):
        shutil.rmtree(str(os.getcwd()) + str(os.sep) + 'pic2asciitemp')
    os.mkdir(str(os.getcwd()) + str(os.sep) + 'pic2asciitemp')

    for zink in range(properseq):
        try:shutil.rmtree(str(os.getcwd()) + str(os.sep) + 'pic2asciitemp' + str(os.sep) + str(int(zink + 1)))
        except:
            try:os.mkdir(str(os.getcwd()) + str(os.sep) + 'pic2asciitemp' + str(os.sep) + str(int(zink + 1)))
            except:
                print('You have a file open or being acsessed in:\n\n' + str(os.getcwd()) + str(os.sep) + 'pic2asciitemp' + str(os.sep) + str(int(zink + 1)) + '\n\nplease close the program that is acsessing this folder and try again.')
                sleep(2)
                print('exiting...')
                sleep(.3)
                exit()
        else:os.mkdir((str(os.getcwd()) + str(os.sep) + 'pic2asciitemp' + str(os.sep) + str(int(zink + 1))))
            

    del zink

    extitems = {}
    for tmp in range(len(list(file_path_list))):
        extitems[tmp] = False
    del tmp

    for thing in range(properseq):
        tmp = open(str(os.getcwd()) + str(os.sep) + 'pic2asciitemp' + str(os.sep) + str(int(thing + 1)) + str(os.sep) + 'tmp' + '.tmp', 'w')
        #tmp.write('[')
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
                    
        #tmp.write(']')
        tmp.close()
    #input('done! press enter to exit')