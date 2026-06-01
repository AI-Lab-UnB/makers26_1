class Circle():
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def __add__(self, c):
        return Circle(self.radius + c.get_radius())

    def __str__(self):
        return f"{self.radius}"

#criação de objetos

c1 = Circle(10)
c2 = Circle(20)

#metodo add e str
c3 = c1 + c2
print(f"Resultado da soma (c3): {c3}") # 30

