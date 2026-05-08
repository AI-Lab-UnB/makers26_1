class Container(object):
    """
    A container object is a list and can store elements of any type
    """
    def __init__(self):
        """
        Initializes an empty list
        """
        self.myList = [];

    def size(self):
        """
        Returns the length of the container list
        """
        return len(self.myList);

    def add(self, elem):
        """
        Adds the elem to one end of the container list, keeping the end
        you add to consistent. Does not return anything
        """
        self.myList.append(elem);

class Stack(Container):
    """
    A subclass of Container. Has an additional method to remove elements.
    """
    def remove(self):
        """
        The newest element in the container list is removed
        Returns the element removed or None if the queue contains no elements
        """
        return self.myList.pop() if self.size() > 0 else None;
        
container = Container();
stack = Stack();

stack.add(0);
stack.add(2);
stack.add(4);

# print the elements in stack
for element in stack.myList:
    print(f'{element} ', end = '');

print("\n");

# remove elements from stack until it is empty and print the elements removed
for i in range(stack.size()):
    print(f'{stack.remove()} ', end = '');



