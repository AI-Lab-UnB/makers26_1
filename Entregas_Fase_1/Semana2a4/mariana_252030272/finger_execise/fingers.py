# Ao testar coloque o pedaço de código em um arquivo separado ou tire """XXXX""" 
#finger 1
"""
a=b=c=1
total = (a + b) * c
print(total)
"""
#finger 2
"""
number = 2
if number > 0:
    print("positive")
elif number == 0:
    print("zero")
else:
    print("negative")
"""
#finger 3
"""
for i in range(int(input())):
    print("hello world")
"""
#finger 4
"""
N = 8
perfect_cubes = 0
i = 0
while(perfect_cubes < N):
    perfect_cubes = i*i*i
    if perfect_cubes == N:
        print("perfect cube")
        break
    i+=1
else:
    print("error")
"""
#finger 5
"""
my_str = "abcdefg"
print("".join(my_str[x] for x in range(0, len(my_str), 2)))
"""
#finger 6
"""
max = 1001
min = 0
integer = 1
count = 1
answer = None
high = 1001
low = 0
integer = 1
count = 1
answer = None

while low <= high:
    mid = (high + low) // 2

    if mid == integer:
        answer = mid
        break

    elif mid > integer:
        high = mid - 1
    else:
        low = mid + 1

    count += 1

print("count:", count)
print("answer:", answer)
"""


#finger 7
"""
def eval_quadratic(a, b, c, x):
    
    # a, b, c: numerical values for the coefficients of a quadratic equation
    # x: numerical value at which to evaluate the quadratic.
    # Returns the value of the quadratic ax² + bx + c.
    
    return a*x**2 + b*x + c

# Examples:    
print(eval_quadratic(1, 1, 1, 1)) # prints 3
def two_quadratics(a1, b1, c1, x1, a2, b2, c2, x2):
    
    # a1, b1, c1: one set of coefficients of a quadratic equation
    # a2, b2, c2: another set of coefficients of a quadratic equation
    # x1, x2: values at which to evaluate the quadratics
    # Evaluates one quadratic with coefficients a1, b1, c1, at x1.
    # Evaluates another quadratic with coefficients a2, b2, c2, at x2.
    # Prints the sum of the two evaluations. Does not return anything.

    return (eval_quadratic(a1, b1, c1, x1) + eval_quadratic(a2, b2, c2, x2))

# Examples:    
#print(two_quadratics(1, 1, 1, 1, 1, 1, 1, 1)) # prints 6
print(two_quadratics(1, 1, 1, 1, 1, 1, 1, 1)) # prints 6 then None
"""
#finger 8
"""
def same_chars(s1, s2):
    # s1 and s2 are strings
    # Returns boolean True is a character in s1 is also in s2, and vice 
    # versa. If a character only exists in one of s1 or s2, returns False.

    for char in s1:
        if char not in s2:
            return False
    for char in s2:
        if char not in s1:
            return False
    return True


# Examples:
print(same_chars("abc", "cab"))     # prints True
print(same_chars("abccc", "caaab")) # prints True
print(same_chars("abcd", "cabaa"))  # prints False
print(same_chars("abcabc", "cabz")) # prints False
"""
#finger 9 
"""
def dot_product(tA, tB):
    
    # tA: a tuple of numbers
    # tB: a tuple of numbers of the same length as tA
    # Assumes tA and tB are the same length.
    # Returns a tuple where the:
    # * first element is the length of one of the tuples
    # * second element is the sum of the pairwise products of tA and tB
    
    return (len(tA), sum(a*b for a, b in zip(tA, tB)))

# Examples:
tA = (1, 2, 3)
tB = (4, 5, 6)   
print(dot_product(tA, tB)) # prints (3,32)
"""
#finger 10
"""
def all_true(n, Lf):
#     n is an int
#     Lf is a list of functions that take in an int and return a Boolean
#     Returns True if each and every function in Lf returns True when called 
#     with n as a parameter. Otherwise returns False. 

    for function in Lf:
        if not function(n):
            return False
    return True
"""
#finger 11
"""
def remove_and_sort(Lin, k):
    # Lin is a list of ints
    #     k is an int >= 0
    # Mutates Lin to remove the first k elements in Lin and 
    # then sorts the remaining elements in ascending order.
    # If you run out of items to remove, Lin is mutated to an empty list.
    # Does not return anything.

    if len(Lin) <= k:
        del Lin[:]
    else:
        del Lin[0:k]
    Lin.sort()
# Examples:
L = [1,6,3]
k = 1
remove_and_sort(L, k)
print(L)   # prints the list [3, 6]
"""
#finger 12
"""
def count_sqrts(nums_list):

    #nums_list: a list
    #Assumes that nums_list only contains positive numbers and that there are no duplicates.
    #Returns how many elements in nums_list are exact squares of elements in the same list, including itself.

    count = 0
    for num in nums_list:

        root = int(num ** 0.5)

        # verifica:
        # 1. se num é quadrado perfeito
        # 2. se a raiz está na lista
        if root * root == num and root in nums_list:
            count += 1

    return count

# Examples:    
print(count_sqrts([3,4,2,1,9,25])) # prints 3
"""
#finger 13
"""
def sum_str_lengths(L):
    soma_atual = 0
    #L is a non-empty list containing either: 
    #* string elements or 
    #* a non-empty sublist of string elements
    #Returns the sum of the length of all strings in L and 
    #lengths of strings in the sublists of L. If L contains an 
    #element that is not a string or a list, or L's sublists 
    #contain an element that is not a string, raise a ValueError.
    for element in L:
        if type(element) is list:
            soma_atual += sum_str_lengths(element)
        elif type(element) is str:
            soma_atual += len(element)
        else:
            raise ValueError
    return soma_atual

    

# Examples:
print(sum_str_lengths(["abcd", ["e", "fg"]]))  # prints 7
print(sum_str_lengths([12, ["e", "fg"]]))      # raises ValueError
print(sum_str_lengths(["abcd", [3, "fg"]])) 
"""
#finger 14
'''
def keys_with_value(aDict, target):

    # aDict: a dictionary
    # target: an integer or string
    # Assume that keys and values in aDict are integers or strings.
    # Returns a sorted list of the keys in aDict with the value target.
    # If aDict does not contain the value target, returns an empty list.
    # Your code here   
    keys = []
    for key in aDict.keys():
        if aDict[key] == target:
            keys.append(key)
    return sorted(keys)
# Examples:
aDict = {1:2, 2:4, 5:2}
target = 2   
print(keys_with_value(aDict, target)) # prints the list [1,5]

def all_positive(d):

    # d is a dictionary that maps int:list
    # Suppose an element in d is a key k mapping to value v (a non-empty list).
    # Returns the sorted list of all k whose v elements sums up to a 
    # positive value.
    # Your code here
    keys = [] 
    for key, values in d.items():
        if sum(values)>0:
            keys.append(key)
    return sorted(keys)

# Examples:
d = {5:[2,-4], 2:[1,2,3], 1:[2]}
print(all_positive(d))   # prints the list [1, 2]
#finger 15
'''
#finger 15
"""
def recur_power(base, exp):
 
    # base: int or float.
    # exp: int >= 0

    # Returns base to the power of exp using recursion.
    # Hint: Base case is when exp = 0. Otherwise, in the recursive
    # case you return base * base^(exp-1).

    # Your code here  
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    return base * recur_power(base, exp-1)

# Examples:
print(recur_power(2,5))  # prints 32
"""
#finger 16
"""
def flatten(L):
    
    #L: a list 
    #Returns a copy of L, which is a flattened version of L 
    
    list_now = []
    for element in L:
        if type(element) is list:
            list_now.extend(flatten(element))
        else:
            list_now.append(element)
    return list_now

# Examples:
L = [[1,4,[6],2],[[[3]],2],4,5]
print(flatten(L)) # prints the list [1,4,6,2,3,2,4,5]
"""
#finger 17
'''
class Circle():
    def __init__(self, radius):
        """ Initializes self with radius """
        self.radius = radius

    def get_radius(self):
        """ Returns the radius of self """
        return self.radius

    def set_radius(self, radius):
        """ radius is a number
        Changes the radius of self to radius """
        self.radius = radius

    def get_area(self):
        """ Returns the area of self using pi = 3.14 """
        return 3.14 * self.radius**2

    def equal(self, c):
        """ c is a Circle object
        Returns True if self and c have the same radius value """
        if self.radius == c.radius:
            return True
        else:
            return False

    def bigger(self, c):
        """ c is a Circle object
        Returns self or c, the Circle object with the bigger radius """
        if self.radius > c.radius:
            return self
        else:
            return c
'''
#finger 18
'''
class Circle():
    def __init__(self, radius):
        """ Initializes self with radius """
        self.radius = radius

    def get_radius(self):
        """ Returns the radius of self """
        return self.radius

    def __add__(self, c):
        """ c is a Circle object 
        Returns a new Circle object whose radius is 
        the sum of self and c's radius """
        return Circle(self.radius+c.radius)

    def __str__(self):
        """ A Circle's string representation is the radius """
        return str(self.radius)
'''
#finger 19
'''
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
        return len(self.myList)

    def add(self, elem):
        """
        Adds the elem to one end of the container list, keeping the end
        you add to consistent. Does not return anything
        """
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
        if self.size() > 0:
            return self.myList.pop()
        else:
            return None
'''    
#finger 20
'''
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
        return len(self.myList)

    def add(self, elem):
        """
        Adds the elem to one end of the container list, keeping the end
        you add to consistent. Does not return anything
        """
        self.myList.append(elem)

class Queue(Container):
    """
    A subclass of Container. Has an additional method to remove elements.
    """
    def remove(self):
        """
        The oldest element in the container list is removed
        Returns the element removed or None if the stack contains no elements
        """
        if self.size() > 0:
            return self.myList.pop(0)
        else:
            return None
'''
#finger 22
## são questões
'''
""" question 1 """
Question 1: Simplify n*n + log(n) + 2**a to determine θ in terms of n.
- n*n = n**2 
- a is constant so 2**a = c
- n**2 + log(n) + c
- o polinomial n**2 custa mais que log(n) e algo constante logo theta(n**2)

""" question 2 """
Question 2: Simplify 2**n + n*log(n) + n**2 to determine θ in terms of n.
- 2**n is exponential is dominant so theta(2**n) is the answer


""" question 3 """
Question 3: Simplify f*log(f) + 100000 + 300*a + x*y*z to determine θ in terms of n.
-  theta(1) porque não tem n na função logo o tempo da função não cresce com n
'''
#finger 23
'''
#Question 1: Choose the worst-case asymptotic order of growth (upper and lower bound) for the following function. Assume n = a.
def running_product(a):
    count = 0
    """ a is an int """
    product = 1
    for i in range(5,a+5):
        count += 1
        product *= i
        if product == a:
            return True, count
    return False, count
#upper bound  = O(n) e lower bound = O(n)
print(running_product(0),
running_product(11),
running_product(10000))
#Question 2: Choose the worst-case asymptotic order of growth (upper and lower bound) for the following function. Assume n = len(L).

def tricky_f(L, L2):
    count = 0
    """ L and L2 are lists of equal length """
    inL = False
    for e1 in L:
        count += 1
        if e1 in L2:
            inL = True
    inL2 = False
    for e2 in L2:
        count +=1
        if e2 in L:
            inL2 = True
    return inL and inL2, count
# upper bound = 2(n*n) = O(n**2)(because in method goes from 0 to n - 1 com n sendo o len(dalista) e o loop passa por todos os elemento 1 vez logo n*n e o dois é pq isso se repete 2 ezes) (n being the lenght of the list), lower bound = n**2
#Question 3: Choose the worst-case asymptotic order of growth (upper and lower bound) for the following function.
print(tricky_f([],[]))

def sum_f(n):
    count = 0
    """ n > 0 """
    answer = 0
    while n > 0:
        answer += n%10
        n = int(n/10)
        count +=1 
    return answer, count
# upperbound = log(n), O(log(n)) = lower bound
print(sum_f(1000), sum_f(10))
'''