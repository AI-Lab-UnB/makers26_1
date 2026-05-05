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
        return self.myList.pop(0)