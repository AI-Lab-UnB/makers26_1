class Container(object):

    def __init__(self):
        self.myList = []

    def size(self):
        return len(self.myList)
    def add(self, elem):
        self.myList.append(elem)
class Queue(Container):

    def remove(self):
        return self.myList.pop(0) if len(self.myList) else None

lista = Queue()
lista.add(1)
lista.add(2)
lista.add(3)
for elemento in lista.myList:
    print(f"{elemento}, ", end='') #1,2,3
print(f"\n{lista.size()}") #3
for i  in range(lista.size()+1):
    print(f'{lista.remove()}, ', end='') #1,2,3, None