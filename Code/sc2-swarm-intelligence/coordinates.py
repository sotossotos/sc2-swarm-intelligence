class Coordinates:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def tupleStyle(self):
        pos=(self.x,self.y)
        return tuple(pos)