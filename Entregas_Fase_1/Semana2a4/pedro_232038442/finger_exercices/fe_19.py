class Container(object):
    """
    An object Container is a list and can store elements of any type
    """
    def __init__(self):
        """
        Initialize an empty list
        """
        self.myList = []

    def size(self):
        """
        Return the length of the container list
        """
        return len(self.myList)

    def add(self, elem):
        """
        Add an element to one end of the container list, keeping
        always the same end for addition. Does not return anything.
        """
        self.myList.append(elem)


class Stack(Container):
    """
    A subclass of Container with an additional method to remove elements.
    """
    def remove(self):
        """
        The most recent element of the container list is removed.
        Return the removed element or None if the stack does not contain elements.
        """
        if self.size() > 0:
            return self.myList.pop()
        else:
            return None