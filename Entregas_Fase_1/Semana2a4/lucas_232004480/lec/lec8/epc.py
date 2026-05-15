# def bisection_root(x,epsilon):
#     low = 0
#     high = x
#     ans = (high + low)/2.0
#     while abs(ans**2 - x) >= epsilon:
#         if ans**2 < x: 
#             low = ans
#         else: 
#             high = ans
#         ans = (high + low)/2.0
#             # print(ans, 'is close to the root of', x)
#     return ans

# print(bisection_root(99,0.1))
# print(bisection_root(100,0.1))
# print(bisection_root(101,0.1))
# print(bisection_root(102,0.1))

# #####
# def calc(op, x, y):
#     return op(x,y)
# def add(a,b):
#     return a+b
# def div(a,b):
#     if b != 0:
#         return a/b
#     return "Denominator was 0."
# print(calc(add, 2, 3))
# print(calc(div, 2, 3))
# print(calc(div, 2, 0))


# def func_a():
#     print('inside func_a')
# def func_b(y):
#     print('inside func_b')
#     return y
# def func_c(f, z):
#     print('inside func_c')
#     return f(z)
# print(func_a())
# print(5 + func_b(2))
# print(func_c(func_b, 3))

def apply(criteria,n):
    count = 0
    for i in range(n+1):
        if criteria(i):
            print(i)
            count +=1
    return count

def is_even(x):
    return x%2==0
print(apply(is_even,10))
