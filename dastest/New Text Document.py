from multiprocessing import Process
#from tkinter import *
def tar():
    print('hello')

if __name__ == '__main__': 
    p1 = Process(target=tar)
    p2 = Process(target=tar)
    p1.start()
    p1.join()
    p2.start()
    p2.join()
