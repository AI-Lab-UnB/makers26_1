class Circle():
    def __init__(self,radius):
        self.r = radius
    def get_radius(self):
        return self.r
    def set_radius(self,radius):
        self.r = radius
    def get_area(self):
        return 3.14 * self.r * self.r
    def equal(self, c):
        if c.r == self.r:
            return True
    def bigger(self, c):
        if c.r > self.r:
            return c
        else:
            return self.r
    