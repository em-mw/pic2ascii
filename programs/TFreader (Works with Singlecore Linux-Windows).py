import os
from sty import fg
from time import time
from click import clear
os.system('')
if str(os.name) == 'nt':
    dirslash = '\\'
else:
    dirslash = '/'
start = int(time())
x = 1
while True:
    try:tf = open(str(os.getcwd()) + str(dirslash) + 'outputTF' + str(dirslash) + str(int(x)) + '.txt', 'r')
    except:break
    print(str(tf.read()))
    tf.close()
    print(str(fg.rs) + 'Frame' + str(x))
    clear()
    x = int(x + 1)
input(str(fg.rs) + '\n\ndone in ' + str(int(time()-start)))