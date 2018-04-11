#Will handel most of the GUI
from Tkinter import *
stuff=[]
class interface(object):
    

    def __init__(self, x, y):        
        self.root=Tk()
        #f=Frame(self.root)
        self.c=Canvas(self.root, width=x*10, height=y*10)
        #self.c=Canvas(f, width=x*10, height=y*10)
        #self.c.pack()
        self.c.create_rectangle(0,0,10,10, fill='red')
        self.v=StringVar()
        self.v.trace('w',self.edited)
        self.start=''
        self.l=Entry(self.root, textvariable=self.v, width=40)
        self.l.bind('<Return>', self.stuff)
        #self.l.pack()
        self.t=Text(self.root, state=DISABLED,height=12, width=40)
        #self.t=Text(f, state=DISABLED, height=10, width=10)
        self.c.grid(row=0)
        self.l.grid(row=1, columnspan=2)
        self.t.grid(row=0, column=1)
        #f.pack(expand=True)
        '''self.c.pack(expand=True, side=LEFT)
        self.l.pack(expand=True)
        self.t.pack(expand=True, side=LEFT)'''
        self.root.mainloop()
        #print "test"
    def stuff(self,event):
        print "Text was " +self.v.get()
    def test_rect(self, x1, y1, x2, y2):
        self.c.create_rectangle(x1,y1, x2, y2, fill='red')
    def what(self):
        print self.v.get()
    def edited(self, *args):
        '''Runs whenever the text is edited, to make sure it starts with the right thing'''
        if self.v.get().startswith(self.start)==False:#test to see if it starts correctly
            #print "edited"
            self.v.set(self.start)#update the string to be the start
            self.l.icursor(len(self.start))#move the cursor to the end of the start
            #doesn't work as well as I had hoped