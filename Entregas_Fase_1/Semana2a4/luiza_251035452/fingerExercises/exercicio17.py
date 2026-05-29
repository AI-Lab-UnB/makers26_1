class Circle():
    
    def __init__(self, radius):
        self.radius = radius  

    def get_radius(self):
        return self.radius  

    def set_radius(self, radius):
        self.radius = radius 

    def get_area(self):
        return 3.14 * (self.radius ** 2)  

    def equal(self, c):
        return self.radius == c.radius  

    def bigger(self, c):
        if self.radius > c.radius:
            return self  
        else:
            return c  

c1 = Circle(2)
c2 = Circle(5)

print(c1.get_radius())  
c1.set_radius(3)
print(c1.get_radius())   
print(c1.get_area())     
print(c1.equal(c2))      
print(c1.bigger(c2))     