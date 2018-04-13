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
    def tick(self, command):
        '''Reads the command and acts on it
        Outputs:
            1:Tick was run, print the world
            0:Game should now quit
            Something else:Print that
        '''
        if command=='':
            self.w.tick()
            return 1
        elif command=='q':
            return 0
        elif command=='d':
            return self.w.diagnose()
    def __repr__(self):
        return str(self.w)
import interface
class master(object):
    def __init__(self):
        ans=raw_input("Use new input? y/N ").strip().lower()
        if ans=='y':
            self.mode='setup'
            self.inter=interface.interface(self, 10,10)
            self.inter.startup()#this call doesn't return until the window is closed, nothing will be run after it
            #print "done!"
            #self.inter.set_text('Enter the setup number')
            #print "New input is not yet coded"
            #self.interface_setup()
            #return
        else:
            ans=raw_input("Enter setup number: ").strip()
            if ans.isdigit()==False:
                ans=0
            else:
                ans=int(ans)
            self.game=game(ans)
            self.mainloop()
    def mainloop(self):
        while True:
            ans=raw_input(">")
            a=self.game.tick(ans)
            if a==0:
                return
            elif a==1:
                print self.game
            elif type(a)==str:
                print a
    def recieve(self, value):
        if self.mode=='setup':
            self.game=game(int(value))
            self.mode='play'
        elif self.mode=='play':
            a=self.game.tick(value)
            if a==0:
                self.inter.end()
            elif a==1:
                self.inter.set_text(str(self.game)) #eventually, will draw it
            elif type(a)==str:
                self.inter.set_text(a)