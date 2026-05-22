class circle ():
    def __init__(self, radius):
        self.radius = radius
    def get_radius(self):
        return self.radius
    def __add__(self, c):
        radius = self.radius + c.radius
        return circle(radius)
    def __str__ (self):
        return str(self.radius)