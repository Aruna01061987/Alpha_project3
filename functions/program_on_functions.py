"""WAP to add 2 nos and return the result
a. use positional as well as keyword only arguments
b.use positional only arguments
c. keyword only arguments"""

#
# def add_(a, /, *, b):
#
#     return a+b
#
# c = add_(1, b=2)
# print(c)



""" list of even numbers """


# def even_numbers(num):
#     l = []
#     for i in range(num):
#         if i % 2 == 0:
#             l.append(i)
#     return l
#
# num = int(input(f"enter the number: "))
# l1 = (even_numbers(num))
#
# print(l1
"""WAF to return all the prime numbers in user defined range."""

# def prime_(end, start=2):
#
#     l= []
#     for n in range(start, end+1):
#         if n>1:
#             for i in range(2, n):
#                 if n % i == 0:
#                     break
#             else:
#                 l.append(n)
#     return l
#
# print(prime_(50))
# print(prime_(50,4))

"""WAF to print fibonacci series in the user defines range"""
#
# a = 0
# b = 1
# i = 0
# while i<10:
#     print(a, end=" ")
#     c = a + b
#     a = b
#     b = c
#     i += 1


def fibonacci_(n, a=0,b=1,i=0):
    while i<n:
        print(a, end=" ")
        c = a + b
        a = b
        b = c
        i += 1

fibonacci_(10)



