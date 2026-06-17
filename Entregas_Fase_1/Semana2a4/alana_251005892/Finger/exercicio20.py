class container(object):
    def _init_(self):
        self.myList = []
    def size(self):
        return len(self.myList)
    def add (self, elem):
        self.myList.append(elem)

class queue (container):
    def remove (self):
        if len(self.myList) ==0:
            return None
        else:
            lista= self.myList.pop(0)
            return lista