class Circle():
    
    def __init__(self, radius):
        self.radius = radius  

    def get_radius(self):
        return self.radius  

    def __add__(self, c):
        novo_raio = self.radius + c.radius  
        return Circle(novo_raio)  

    def __str__(self):
        return str(self.radius)  

# testes
c1 = Circle(2)
c2 = Circle(3)

c3 = c1 + c2 
print(c3)    