class circle ():
    def _init_(self, radius):
        self.radius = radius
    def get_radius(self):
        return self.radius
    def _add_(self, c):
        radius = self.radius + c.radius
        return circle(radius)
    def _str_ (self):
        return str(self.radius)