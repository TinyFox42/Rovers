import math
tile_size=100
class id_manager(object):
    curr_id=0
    def next_id(self):
        val=self.curr_id
        self.curr_id+=1
        return val
ids=id_manager()
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
        struc.assign_world(self)
    def __str__(self):
        for floor in self.floors:
            x=(floor.x)/tile_size
            y=(floor.y)/tile_size
            if not (0<=x<self.x and 0<=y<self.y):
                print "Something is out of bounds"
                continue
            sprite=floor.sprite
            self.view[y][x]=sprite
        for struc in self.structures:
            x=int(struc.x)/tile_size#because the plan is to later on move away from just printing stuff. This works for now
            y=int(struc.y)/tile_size
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
        self.check_collisions()
        for i in range(len(self.structures))[::-1]:#destroy dead stuff
            if self.structures[i].ded:
                self.structures.pop(i)
    def check_collisions(self):
        pass
        for i,a in enumerate(self.structures):
            for b in self.structures[i+1:]:
                print "%s and %s"%(a.sId, b.sId)
                x=False
                y=False
                if ((b.x+b.size)>=(a.x+a.size)>(b.x))or((b.x+b.size)>(a.x)>=(b.x)):
                    x=True
                if ((b.y+b.size)>=(a.y+a.size)>(b.y))or((b.y+b.size)>(a.y)>=(b.y)):
                    y=True
                if x and y:
                    print "%s hit %s"%(a.sId, b.sId)
                    a.ded, b.ded=True, True#later on, replace this with some actual special colision interaction
class null_world(object):
    '''Has all the functions needed for an object to be tested, without actually being a world'''
    pass
class floor(object):
    def __init__(self, x, y, sprite):
        self.x=x*tile_size
        self.y=y*tile_size
        self.sprite=sprite
        
class ground(floor):
    def __init__(self, x, y):
        floor.__init__(self, x, y, '.')
class structure(object):
    def __init__(self, x, y, sprite, box_length):
        self.x=x*tile_size
        self.y=y*tile_size
        self.sprite=sprite
        self.owner=null_world() #ok, that just sounds cool to type
        self.sId=ids.next_id()
        self.size=box_length*tile_size
        self.ded=False
    def tick(self):
        pass
    def assign_world(self, world):
        self.world=world
class rock(structure):
    def __init__(self, x,y):
        structure.__init__(self,x,y,"*",1)
class boulder(structure):
    def __init__(self, x, y, speedx, speedy, friction):
        structure.__init__(self, x, y, "o",1)
        self.dx=speedx
        self.dy=speedy
        self.k=friction
    def tick(self): #needed to think back to physics to write this function
        if (abs(self.dx)>tile_size or abs(self.dy)>tile_size):
            print "Warning, an object is moving fast enough to suffer relativistic effects."
        self.x+=self.dx
        self.y+=self.dy
        if (self.dx==0 and self.dy==0):
            return
        thet=math.atan2(self.dy, self.dx)
        d=math.sqrt(self.dx**2+self.dy**2)
        d-=(1.0*self.k)/tile_size #did I really forget to do this?
        if d<0:  #I feel like I may want to do some editing to this to make the friction/speed scale with tile_size
            d=0
        self.dx=(d*math.cos(thet))
        self.dy=(d*math.sin(thet))
    def test_ticks(self):
        while True:
            self.tick()
            print "x:%d, y:%d, pos:(%d, %d), dx:%f, dy:%f"%(self.x,self.y,self.x/tile_size,self.dy/tile_size,self.dx,self.dy)
            if raw_input(""):
                break
    def test_run(self):
        print "Start: x:%3d, y:%d, pos:(%d, %d), dx:%f, dy:%f"%(self.x,self.y,self.x/tile_size,self.dy/tile_size,self.dx,self.dy)
        a=0
        while self.dx!=0 or self.dy!=0:
            self.tick()
            a+=1
            if a%10==0:
                print "After %3d ticks: x:%d, y:%d, pos:(%d, %d), dx:%f, dy:%f"%(a,self.x,self.y,self.x/tile_size,self.dy/tile_size,self.dx,self.dy)
        print "Finished after %3d ticks: x:%d, y:%d, pos:(%d, %d), dx:%f, dy:%f"%(a,self.x,self.y,self.x/tile_size,self.dy/tile_size,self.dx,self.dy)