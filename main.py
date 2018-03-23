import world
class game(object):
    def __init__(self, setup=0):
        self.w=world.world()
        if setup==0:
            self.w.ground()
        elif setup==1:
            self.setup_ball_wall_coll()
    def run(self):
        cont=True
        while(cont):
            print self.w
            ans=raw_input("")
            if ans=="q":
                break
            self.w.tick()
    def setup_ball_wall_coll(self):
        a=world.boulder(0,0,25,0,0)
        b=world.rock(2,0)
        self.w.ground()
        self.w.add_struc(a)
        self.w.add_struc(b)
        print self.w