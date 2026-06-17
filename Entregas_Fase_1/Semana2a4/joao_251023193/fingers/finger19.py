class Container(object):
    """
    A container object is a list and can store elements of any type
    """
    def __init__(self):
        """
        Initializes an empty list
        """
        self.myList = []
    def size(self):
        """
        Returns the length of the container list
        """
        # Your code here
        
        return len(self.myList)
        
    def add(self, elem):
        """
        Adds the elem to one end of the container list, keeping the end
        you add to consistent. Does not return anything
        """
        # Your code here
        
        self.myList.append(elem)
        
class Stack(Container):
    """
    A subclass of Container. Has an additional method to remove elements.
    """
    def remove(self):
        """
        The newest element in the container list is removed
        Returns the element removed or None if the queue contains no elements
        """
        # Your code here
        
        if self.size() > 0:
            return self.myList.pop()
        return None
        