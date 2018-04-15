import math
tile_size=100
class id_manager(object):
    curr_id=0
    def next_id(self):
        val=self.curr_id
        self.curr_id+=1
        return val
ids=id_manager()
class floor(object):
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
        #self.owner=null_world() #ok, that just sounds cool to type
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
        return val