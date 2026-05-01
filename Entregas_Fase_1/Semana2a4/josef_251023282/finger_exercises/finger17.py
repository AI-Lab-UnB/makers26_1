class Circle():
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
            return self.radius
    
    def set_radius(self, radius):
         self.radius = radius

    def get_area(self):
         return 3.14 * (self.radius**2)
    
    def equal(self,c):
         return self.radius == c.get_radius()
    
    def bigger(self,c):
         if self.radius >= c.get_radius():
              return self
         else:
            return c
         
