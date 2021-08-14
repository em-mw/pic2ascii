import more, os

x = open(os.getcwd() + 'this.txt', 'w')
x.write('this is the best')
x.close()

#more.truncate_utf8_chars(os.getcwd() + 'this.txt', 1)
input(os.getcwd())

os.system('notepad this.txt')
