class world(object):
    def __init__(self, x=10, y=10):
        '''Makes a new world object, with dimensions x and y'''
        self.floors=[]
        self.structures=[]
        self.x=x
        self.y=y
        self.view=[[""]*x]*y
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
            sprite=floor.sprite
            self.view[y][x]=sprite
        for struc in self.structures:
            x=struc.x
            y=struc.y
            sprite=struc.sprite
            self.view[y][x]=sprite
        val=""
        for y in range(self.y):
            for x in range(self.x):
                val+=self.view[y][x]
            val+="\n"
        return val

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
class rock(structure):
    def __init__(self, x,y):
        structure.__init__(x,y,"*")