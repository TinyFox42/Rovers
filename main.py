import world
class game(object):
    def __init__(self, setup=0):
        self.w=world.world()
        if setup==0:
            self.w.ground()
        elif setup==1:
            self.setup_ball_wall_coll()
        else:
            try:
                exec "self.setup_"+str(setup)+"()"
            except NameError:
                print "Non-existant setup"
                print "Defaulting to basic setup"
                self.w.ground()
    def run(self):
        cont=True
        while(cont):
            print self.w
            ans=raw_input("")
            if ans=="q":
                break
            if ans=='d':
                self.w.diagnose()
            self.w.tick()
    def setup_ball_wall_coll(self):
        a=world.boulder(0,0,25,0,0)
        b=world.rock(2,0)
        self.w.ground()
        self.w.add_struc(a)
        self.w.add_struc(b)
        print self.w
    def setup_2(self):
        wall=world.rock(5,5)
        left=world.boulder(0,5,25,0,0)
        top=world.boulder(5,0,0,20,0)
        right=world.boulder(10,5,-13,0,0)
        bottom=world.boulder(5,10,0,-7,0)
        self.w.ground()
        self.w.add_struc(wall)
        self.w.add_struc(left)
        self.w.add_struc(top)
        self.w.add_struc(right)
        self.w.add_struc(bottom)
        print self.w
        #if raw_input("Good? ").strip().lower()=='y':
        self.run()