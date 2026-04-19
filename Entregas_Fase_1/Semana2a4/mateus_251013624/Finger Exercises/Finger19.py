class Container(object):

    def __init__(self):
        self.myList = []

    def size(self):
        return len(self.myList)
    def add(self, elem):
        self.myList.append(elem)
class Stack(Container):

    def remove(self):
        return self.myList.pop() if len(self.myList) else None

lista = Stack()
lista.add(1)
lista.add(2)
lista.add(3)
for elemento in lista.myList:
    print(f"{elemento}, ", end='') #1,2,3
print(f"\n{lista.size()}") #3
for i  in range(lista.size()+1):
    print(f'{lista.remove()}, ', end='') #3,2,1, None
