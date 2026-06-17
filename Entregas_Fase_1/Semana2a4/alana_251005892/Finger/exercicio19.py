class conteiner(object):
    def _init_ (self):
        self.myList = []
    def size (self):
        return len(self.myList)
    def add (self, elem):
        self.myList.append(elem)

class stack(conteiner):
    def remove(self):
        if len(self.myList) == 0:
            return None
        else:
            item = self.myList.pop()
            return item