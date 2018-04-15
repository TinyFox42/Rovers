#Will handel most of the GUI
scale=10#How many tiles there are per side
from Tkinter import *
class interface(object):
    

    def __init__(self, master, x, y):  
        self.master=master      
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
        self.l.bind('<Return>', self.send_up)
        #self.l.pack()
        #self.t=Text(self.root, state=NORMAL,height=12, width=40)
        self.make_text_box()#sets up the textbox, removes some clutter from the main function
        self.t.mark_set("start", INSERT)
        self.t.mark_gravity("start", LEFT)
        self.t.insert(INSERT, 'Enter setup number:')
        self.t.config(state=NORMAL)
        #self.t=Text(f, state=DISABLED, height=10, width=10)
        self.c.grid(row=0, sticky='nsew')
        self.l.grid(row=1, columnspan=2, sticky='we')
        #self.t.grid(row=0, column=1, sticky='nsew')
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=0)
        #f.pack(expand=True)
        '''self.c.pack(expand=True, side=LEFT)
        self.l.pack(expand=True)
        self.t.pack(expand=True, side=LEFT)'''
        #self.root.mainloop()
        #print "test"
    def make_text_box(self):
        frame=Frame(self.root, bd=2, relief=SUNKEN)
        frame.grid_rowconfigure(0,weight=1)
        frame.grid_columnconfigure(0,weight=1)
        scrollbar=Scrollbar(frame)
        scrollbar.grid(row=0,column=1,sticky='ns')
        self.t=Text(frame, yscrollcommand=scrollbar.set, state=NORMAL,height=12, width=40)
        self.t.grid(row=0,column=0,sticky='nsew')
        scrollbar.config(command=self.t.yview)
        frame.grid(row=0,column=1,sticky='nsew')
    def startup(self):
        self.root.mainloop()
    def stuff(self,event):
        print "Text was " +self.v.get()
        self.set_text(self.v.get())
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
    def set_text(self, text):
        self.t.config(state=NORMAL)
        self.t.delete('start', END)
        self.t.insert(END, text)
        self.t.config(state=DISABLED)
    def set_prefix(self, prefix):
        self.v.set(prefix)
        self.start=prefix
    def send_up(self, event):
        value=self.v.get()
        value=value[len(self.start):]
        self.master.recieve(value)
        self.v.set('')
    def end(self):
        self.root.destroy()
    def draw(self, tile, floors, strucs):
        width=int(self.c.config()['width'][4])
        height=int(self.c.config()['height'][4])
        #print width
        #print height
        scalex=1.0*width/scale
        ratiox=scalex/tile
        scaley=1.0*height/scale
        ratioy=scaley/tile
        #ratio=1.0*scale/tile
        #print self.c.config()['height']
        #print ratio
        for floor in floors:
            self.c.create_rectangle(max(floor[0]*ratiox,0),max(floor[1]*ratioy,0),min(floor[0]*ratiox+scalex,width),min(floor[1]*ratioy+scaley,height),fill=floor[2])
        for struc in strucs:
            self.c.create_rectangle(max(struc[0]*ratiox,0),max(struc[1]*ratioy,0),min(struc[0]*ratiox+struc[2]*ratiox,width),min(struc[1]*ratioy+struc[2]*ratioy,height),fill=struc[3])
        