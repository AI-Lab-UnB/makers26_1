class Circle():
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_radius(self, radius):
        self.radius = radius

    def get_area(self):
        pi = 3.14
        return (self.get_radius()**2 * pi)
        
    def equal(self, c):
        return (self.get_radius() == c.get_radius())
        
    def bigger(self, c):
        if self.get_radius() > c.get_radius():
            bigger = self
        else:
            bigger = c
        return (bigger)