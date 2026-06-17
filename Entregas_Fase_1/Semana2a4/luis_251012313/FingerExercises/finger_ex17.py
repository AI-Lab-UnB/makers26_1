import math;

class Circle():
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius;

    def set_radius(self, radius):
        self.radius = radius;

    def get_area(self):
        return math.pi * self.radius ** 2;

    def equal(self, c):
        return self.radius == c.get_radius();
    
    def bigger(self, c):
        return self if (self.radius > c.get_radius()) else c;

# instance creation

c1 = Circle(2);
c2 = Circle(4);

print("="*30);
print("="*30);

# get_radius
print("-"*30);
print(f'Radius of c1: {c1.get_radius()}');
print(f'Radius of c2: {c2.get_radius()}');
print("-"*30);

# set_radius
c1.set_radius(3);
print(f'New radius of c1: {c1.get_radius()}');
print("-"*30);

# get_area
print(f'Area of c1: {c1.get_area():.2f}');

# get_area of c2
print(f'Area of c2: {c2.get_area():.2f}');
print("-"*30);

# equal
print(f'c1 and c2 are equal: {c1.equal(c2)}');
print("-"*30);

# bigger
bigger_circle = c1.bigger(c2);
print(f'The bigger circle has radius: {bigger_circle.get_radius()}');
print("-"*30);