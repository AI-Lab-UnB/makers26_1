import math


class Circle():
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
            return self.radius
    def set_radius(self, radius):
        self.radius = radius
    def get_area(self):
        return self.radius * self.radius * math.pi
    def equal(self, c):
        return self.radius == c.radius
    def bigger(self, c):
        return self if self.radius > c.radius else c

#Criação de objetos
circulo_a = Circle(5)
circulo_b = Circle(10)
circulo_c = Circle(5)

#get_radius
print(f"Raio inicial A: {circulo_a.get_radius()}") # 5
print(f"Raio inicial B: {circulo_b.get_radius()}") # 10

#get_area
print(f"Área do Círculo A: {circulo_a.get_area():.2f}") #78.54
print(f"Área do Círculo B: {circulo_b.get_area():.2f}") #314.15

#equal
print(f"O Círculo A é igual ao C? {circulo_a.equal(circulo_c)}") # True
print(f"O Círculo A é igual ao B? {circulo_a.equal(circulo_b)}") # False

#bigger
maior = circulo_a.bigger(circulo_b)
print(f"O raio do maior círculo entre A e B é: {maior.get_radius()}") #10

#set_radius
circulo_a.set_radius(20)
print(f"Novo raio de A após modificação: {circulo_a.get_radius()}") #20

#testando o raio alterado
novo_maior = circulo_a.bigger(circulo_b)
print(f"Agora o maior entre A e B é o de raio: {novo_maior.get_radius()}") # 20