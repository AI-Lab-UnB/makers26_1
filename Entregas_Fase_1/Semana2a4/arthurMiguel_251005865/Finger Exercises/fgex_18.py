class Circle():
    def __init__(self,radius):
        self.r = radius
    def getRadius(self):
        return self.r
    def add(self,c):
        return self.r + c.r
    def str(self):
        return str(self.r)
    