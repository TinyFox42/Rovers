#Will handel most of the GUI
from Tkinter import *
class interface(object):
    def __init__(self, x, y):        
        self.root=Tk()
        self.c=Canvas(self.root, width=x*10, height=y*10)
        self.c.pack()
        self.c.create_rectangle(0,0,10,10, fill='red')
        self.root.mainloop()
    def test_rect(self, x1, y1, x2, y2):
        self.c.create_rectangle(x1,y1, x2, y2, fill='red')
    