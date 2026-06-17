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

class Queue(Container):
    """
    A subclass of Container. Has an additional method to remove elements.
    """
    def remove(self):
        """
        The oldest element in the container list is removed
        Returns the element removed or None if the stack contains no elements
        """
        return self.myList.pop(0) if self.size() > 0 else None;

container = Container();
queue = Queue();

queue.add(1);
queue.add(3);
queue.add(5);

# print the elements in queue
for element in queue.myList:
    print(f'{element} ', end = '');
print("\n");

# remove elements from queue until it is empty and print the elements removed
for i in range(queue.size()):
    print(f'{queue.remove()} ', end = '');