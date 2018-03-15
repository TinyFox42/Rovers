import world
class game(object):
    def __init__(self):
        self.w=world.world()
        self.w.ground()
    def run(self):
        cont=True
        while(cont):
            print self.w
            ans=raw_input("")
            if ans=="q":
                break
            self.w.tick()