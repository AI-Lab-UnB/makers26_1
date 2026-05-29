class Container(object):
    
    def __init__(self):
        self.myList = [] 

    def size(self):
        return len(self.myList)  

    def add(self, elem):
        self.myList.append(elem)  


class Stack(Container):
    
    def remove(self):
        if self.size() == 0:  
            return None
        else:
            return self.myList.pop()  


s = Stack()

s.add(10)
s.add(20)
s.add(30)

print(s.size())    
print(s.remove())  
print(s.remove())  
print(s.remove())  
print(s.remove())  