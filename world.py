import elements as els
comm_creators={'floor':els.floor,
                'ground':els.ground,
                'structure':els.structure,
                'rock':els.rock,
                'boulder':els.boulder}
tile_size=100 #how many processed units are in the displayed unit, both with tile dimensions and time
collision_efficiency=.5 #how much of the velocity stays when a boulder and rock collide
'''class id_manager(object):
    curr_id=0
    def next_id(self):
        val=self.curr_id
        self.curr_id+=1
        return val
ids=id_manager()'''
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
                self.floors.append(els.ground(i,j))
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
                #print "%s and %s"%(a.sId, b.sId)
                x=False
                y=False
                if ((b.x+b.size)>=(a.x+a.size)>(b.x))or((b.x+b.size)>(a.x)>=(b.x)):
                    x=True
                if ((b.y+b.size)>=(a.y+a.size)>(b.y))or((b.y+b.size)>(a.y)>=(b.y)):
                    y=True
                if x and y:
                    print "%s hit %s"%(a.sId, b.sId)
                    calculate_collision(a,b)
                    #a.ded, b.ded=True, True#later on, replace this with some actual special colision interaction
    def diagnose(self):
        val=''
        for stu in self.structures:
            val+='\n'+stu.diagnose()
        return val
    def fancy_print(self):
        '''Returns the values needed to draw it'''
        floors=[]
        for flr in self.floors:
            floors.append([flr.x,flr.y,flr.color])
        structures=[]
        for stu in self.structures:
            structures.append([stu.x,stu.y,stu.size,stu.color])
        return tile_size, floors, structures
    def spawn(self, command):
        pass
        parts=command.split(' ')
        if parts[1] in comm_creators.keys():
            comm=" ".join(parts[2:])
            a=comm_creators[parts[1]].from_comm(comm)
            if not a:
                return "Invalid command"
            if a.is_floor():
                print "Now I need to rework the floor system... :("
            else:
                self.add_struc(a)
        else:
            print "make sure that the second word is a element name"
            return 1
        return 1
def calculate_collision(a,b):
    if a.coll=='ball':
        if b.coll=='ball':
            coll_b_b(a,b)
        elif b.coll=="wall":
            coll_b_w(a,b)
    elif a.coll=='wall':
        if b.coll=='ball':
            coll_b_w(b,a)
        elif b.coll=='wall':
            coll_w_w(a,b)
def coll_b_b(a,b):
    print "Ball-ball collisions are not yet coded"
    a.ded, b.ded=True, True
    return
def coll_b_w(a,b):
    '''Calculates what happens in a colision betweel ball a and wall b'''
    #print "Ball-wall collisions are not yet coded"
    #a.ded, b.ded=True, True
    #return
    #most of this assumes that b is statinary, but it shouldn't actually break if b isn't
    farx=False #a hit b, but the part of a that hit was on x+size, not x. Look at the drawing I made below
    fary=False
    '''
    fary=False
(x,y)       (x+size, y)
    _________
    |       |
farx|       | farx=True
=0  |       |
    |_______|
(x,y+size)  (x+size, y+size)
    fary=True
    '''
    if (b.x<(a.x+a.size)<=(b.x+b.size)):
        farx=True#otherwise, either there wasn't a collision (which means this wouldn't be called) or it was at normal x
    if (b.y<(a.y+a.size)<=(b.y+b.size)):fary=True;
    #I guess this also assumes that only one corner on each is intercepting... Which should be true for awhile
    rdx=abs(a.last_tick['dx']-b.dx) #I guess if b ever does move, this will need to be switched to it's previous tick
    rdy=abs(a.last_tick['dy']-b.dy)
    rx,ry=0,0
    if not(b.x<=a.last_tick['x']<(b.x+b.size)):#if last tick it wasn't inside the thing
        rx=a.last_tick['x']-(b.x+b.size)
    elif farx and not (b.x<(a.last_tick['x']+a.size)<=(b.x+b.size)):#if the far side wasn't inside the thing last tick
        rx=b.x-(a.last_tick['x']+a.size)
    if not(b.y<=a.last_tick['y']<(b.y+b.size)):
        ry=a.last_tick['y']-(b.y+b.size)
    elif fary and not (b.y<(a.last_tick['y']+a.size)<=(b.y+b.size)):
        ry=b.y-(a.last_tick['y']+a.size)
    rx=abs(rx)
    ry=abs(ry)
    tx,ty=0,0
    if rdx!=0:
        tx=rx/rdx #the time it takes for the x's to intercept
    if rdy!=0:
        ty=ry/rdy 
    if (tx>=ty):#If it collided along the side where x is constant
        pass
        side='left'
        if farx: side='right';
        print "%s collided with %s on the %s side"%(a.sId, b.sId, side);
        if side=='left':
            a.dx=-(a.dx*collision_efficiency)
            a.x=b.x+b.size
        else:
            a.dx=-(a.dx*collision_efficiency)
            a.x=b.x-a.size
    if tx<=ty:
        side='top'
        if fary:side='bottom';
        print "%s collided with %s on the %s"%(a.sId, b.sId, side);
        if side=='top':
            a.dy=-(a.dy*collision_efficiency)
            a.y=b.y+b.size
        else:
            a.dy=-(a.dy*collision_efficiency)
            a.y=b.y-a.size
    '''elif tx==ty:
        sidey='upper'
        sidex='left'
        if farx: sidex='right';
        if fary: sidey='lower';
        print "Oh, great. %s collided with %s on the %s-%s side..."%(a.sId, b.sId, sidey,sidex)
        print "I don't know what to do now..."
        a.ded, b.ded=True, True'''
    print "t's: \n\tx:%f\n\ty:%f\nfars:\n\tx:%s\n\ty:%s\nr's:\n\tx:%f\n\ty:%f\n\tdx:%f\n\tdy:%f"%(tx,ty,str(farx),str(fary),rx,ry,rdx,rdy)
def coll_w_w(a,b):
    print "Wall-wall collisions are not yet coded"
    a.ded, b.ded=True, True
    return
'''class floor(object):
    def __init__(self, x, y, sprite, color):
        self.x=x*tile_size
        self.y=y*tile_size
        self.sprite=sprite
        self.color=color
class ground(floor):
    def __init__(self, x, y):
        floor.__init__(self, x, y, '.', 'white')
class structure(object):
    type_name="Generic structure"
    def __init__(self, x, y, sprite,color, box_length, collision_class):
        self.x=x*tile_size
        self.y=y*tile_size
        self.sprite=sprite
        self.owner=null_world() #ok, that just sounds cool to type
        self.sId=ids.next_id()
        self.size=box_length*tile_size
        self.ded=False
        self.coll=collision_class
        self.color=color
        #need to add in dx and dy eventually
    def tick(self):
        pass
    def assign_world(self, world):
        self.world=world
    def diagnose(self):
        val= self.type_name+" with sId "+str(self.sId)
        varbs=['x','y','sprite','sId','size','ded','coll_class']
        vals=[self.x,self.y,self.sprite,self.sId,self.size,self.ded,self.coll]
        for i in range(len(varbs)):
            val+= "\n\t%s: %s"%(str(varbs[i]),str(vals[i]))
        return val
class rock(structure):
    type_name="Rock"
    def __init__(self, x,y, sprite='*',color='black', box_length=1, collision_class='wall'):
        structure.__init__(self,x,y,sprite,color,box_length, collision_class)
        self.dx,self.dy=0,0
    def diagnose(self):
        val=structure.diagnose(self)
        varbs=['dx','dy']
        vals=[self.dx,self.dy]
        for i in range(len(varbs)):
            val+= "\n\t%s: %s"%(str(varbs[i]),str(vals[i]))
        return val
class boulder(structure):
    type_name="Boulder"
    def __init__(self, x, y, speedx, speedy, friction, sprite='o',color='brown', box_length=1, collision_class='ball'):
        structure.__init__(self, x, y, sprite,color,box_length,collision_class)
        self.dx=speedx
        self.dy=speedy
        self.k=friction
        self.last_tick={'x':self.x, 'y':self.y, 'dx':self.dx, 'dy':self.dy}
    def tick(self): #needed to think back to physics to write this function
        self.last_tick={'x':self.x, 'y':self.y, 'dx':self.dx, 'dy':self.dy}#for a bit this was at the top...
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
        self.dx=round((d*math.cos(thet)),10)
        self.dy=round((d*math.sin(thet)),10)#the round fixes a few floating-point errors
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
    def diagnose(self):
        val=structure.diagnose(self)
        varbs=['dx','dy','k']
        vals=[self.dx,self.dy,self.k]
        for i in range(len(varbs)):
            val+= "\n\t%s: %s"%(str(varbs[i]),str(vals[i]))
        return val'''