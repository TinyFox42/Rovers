import math
class world(object):
    def __init__(self, x=10, y=10):
        '''Makes a new world object, with dimensions x and y'''
        self.floors=[]
        self.structures=[]
        self.x=x
        self.y=y
        self.view=[]
        for i in range(y):
            self.view.append(['']*x)
    def ground(self):
        '''Fills in the grid with blank floors'''
        for i in range(self.x):
            for j in range(self.y):
                self.floors.append(ground(i,j))
    def add_struc(self, struc):
        self.structures.append(struc)
    def __str__(self):
        for floor in self.floors:
            x=floor.x
            y=floor.y
            if not (0<=x<self.x and 0<=y<self.y):
                print "Something is out of bounds"
                continue
            sprite=floor.sprite
            self.view[y][x]=sprite
        for struc in self.structures:
            x=struc.x
            y=struc.y
            if not (0<=x<self.x and 0<=y<self.y):
                print "Something is out of bounds"
                continue
            sprite=struc.sprite
            self.view[y][x]=sprite
        val=""
        for y in range(self.y):
            for x in range(self.x):
                val+=self.view[y][x]
            val+="\n"
        return val
    def tick(self):
        for struc in self.structures:
            struc.tick()
class floor(object):
    def __init__(self, x, y, sprite):
        self.x=x
        self.y=y
        self.sprite=sprite
        
class ground(floor):
    def __init__(self, x, y):
        floor.__init__(self, x, y, '.')

class structure(object):
    def __init__(self, x, y, sprite):
        self.x=x
        self.y=y
        self.sprite=sprite
    def tick(self):
        pass
class rock(structure):
    def __init__(self, x,y):
        structure.__init__(self,x,y,"*")
class boulder(structure):
    def __init__(self, x, y, speedx, speedy, friction):
        structure.__init__(self, x, y, "o")
        self.dx=speedx
        self.dy=speedy
        self.k=friction
    def tick(self): #needed to think back to physics to write this function
        self.x+=self.dx
        self.y+=self.dy
        if (self.dx==0 and self.dy==0):
            return
        thet=math.atan2(self.dy, self.dx)
        d=math.sqrt(self.dx**2+self.dy**2)
        d-=self.k #did I really forget to do this?
        if d<0:
            d=0
        self.dx=int(d*math.cos(thet))
        self.dy=int(d*math.sin(thet))
    def test_ticks(self):
        while True:
            self.tick()
            print "x:%d, y:%d, dx:%d, dy:%d"%(self.x,self.y,self.dx,self.dy)
            if raw_input(""):
                break