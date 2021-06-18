import shutil, os

pork = int(3)
for chick in range(pork):
    os.mkdir(os.getcwd() + '\\' + str(int(chick + 1)))
shutil.rmtree(os.getcwd() + '\\' + str(pork))