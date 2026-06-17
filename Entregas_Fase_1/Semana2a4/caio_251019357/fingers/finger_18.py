
class Circle():
    def __init__(self, radius):
        """ Initializes self with radius """
        self.radius = radius 

    def get_radius(self):
        """ Returns the radius of self """
        return self.radius

    def __add__(self, c):
        """ c is a Circle object 
        Returns a new Circle object whose radius is 
        the sum of self and c's radius """
        radius_c = c.get_radius()        
        
        return Circle( self.radius + radius_c)

    def __str__(self):
        """ A Circle's string representation is the radius """
        return f"Raio = {self.get_radius()}"



#teste

c_1 = Circle(10)

c_2 = Circle(20)

c_3 = c_1 + c_2

print(c_3)
