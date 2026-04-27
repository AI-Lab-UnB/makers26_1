class Circle():
    def __init__(self, radius):
        self.radius = radius
        
    def get_radius(self):
        return self.radius

    def __add__(self, c):
        return Circle(self.get_radius() + c.get_radius())

    def __str__(self):
        return str(self.get_radius())