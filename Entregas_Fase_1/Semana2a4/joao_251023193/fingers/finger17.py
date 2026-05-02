class Circle():
    
    def __init__(self, radius):
        """ Initializes self with radius """
        # your code here
        
        self.radius = radius
        
    def get_radius(self):
        """ Returns the radius of self """
        # your code here
        
        return self.radius
        
    def set_radius(self, radius):
        """ radius is a number
        Changes the radius of self to radius """
        
        self.radius = radius
        
        # your code here
    def get_area(self):
        """ Returns the area of self using pi = 3.14 """
        
        
        return 3.12 * (self.radius**2)
        
        # your code here
    def equal(self, c):
        """ c is a Circle object
        Returns True if self and c have the same radius value """
        
        if self.radius == c.radius:
            return True
        else:
            return False
        
        # your code here
    def bigger(self, c):
        """ c is a Circle object
        Returns self or c, the Circle object with the bigger radius """
        
        if self.radius < c.radius:
            return c
        elif self.radius > c.radius:
            return self
        
        # your code here
