class Circle():
    def __init__(self, radius):
        self.radius = radius;

    def get_radius(self):
        return self.radius;

    def __add__(self, c):
        return Circle(self.radius + c.get_radius());

    def __str__(self):
        return f'Circle with radius: {self.radius}';

# instance creation

c1 = Circle(2);
c2 = Circle(4);

# add c1 and c2 making use of the __add__ method
# this will create a new Circle instance with the radius equal to the sum of the radius of c1 and c2 

c3 = c1 + c2;

print(c3);
    
