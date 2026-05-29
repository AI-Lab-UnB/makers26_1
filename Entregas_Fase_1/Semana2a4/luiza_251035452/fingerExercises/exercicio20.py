class Container(object):
    
    def __init__(self):
        self.myList = []  

    def size(self):
        return len(self.myList)  

    def add(self, elem):
        self.myList.append(elem)  


class Queue(Container):
    
    def remove(self):
        if self.size() == 0:  
            return None
        else:
            return self.myList.pop(0)  



q = Queue()

q.add(10)
q.add(20)
q.add(30)

print(q.size())    
print(q.remove())  
print(q.remove())  
print(q.remove())  
print(q.remove())  