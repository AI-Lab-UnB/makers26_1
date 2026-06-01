class Container(object):
    def __init__(self):
        self.myList = []
    def size(self):
        return len(self.myList)
    def add(self, elem):
        self.myList.append(elem)

class Stack(Container):
    def Queue(self):
        if self.size() > 0:
            return self.myList.pop(0)
        return None