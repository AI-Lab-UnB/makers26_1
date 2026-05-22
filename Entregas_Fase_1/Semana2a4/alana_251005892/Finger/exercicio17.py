class circle():
    def __init__ (self,radius):
        self.radius = radius
    def get_radius(self):
        return self.radius
    def set_radius(self, radius):
        self.radius = radius
    def get_area(self):
        return 3.14 * self.radius ** 2
    def equal (self, c):
        return self.radius == c.radius
    def bigger(self, c):
        if c.radius>=self.radius:
            return c
        else:
            return self