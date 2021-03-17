from tkinter import *
from tkinter import messagebox
#root = Tk()
#root.eval('tk::PlaceWindow %s center' % root.winfo_toplevel())
#root.withdraw()
#root.attributes('-alpha', 0)

#messagebox.showerror('Invalid Directory', str('The Directory \'%s\' is invalid' % 'sdf'))

#root.deiconify()
#root.destroy()
#root.quit()



root = Tk()
root.eval('tk::PlaceWindow %s center' % root.winfo_toplevel())
root.withdraw()
root.attributes('-alpha', 0)

messagebox.showerror('Not suppored Image type', str('This image type is not valid!\nThe only valid image types are .jpg and .jpeg'))

root.deiconify()
root.destroy()
root.quit()
del root