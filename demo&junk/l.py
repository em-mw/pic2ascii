from subprocess import Popen
for x in [0,1,2]:
    Popen(['xterm', '-e', 'xterm'])
input('I am done here')
