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
#
#
# def fibonacci_(n, a=0,b=1,i=0):
#     while i<n:
#         print(a, end=" ")
#         c = a + b
#         a = b
#         b = c
#         i += 1
#
# fibonacci_(10)


"""variable positional arguments"""


# def pos_args(*args):
#     count = 0
#     for i in args:
#         count += 1
#     return count
#
# print(pos_args(1,2,3,4))
#
# def function(*args):
#     return len(args)
#
# print(function(1,2,3,4))


"""WAF that takes variable no of positional arguments and returns all the integer values"""

#
# def function_(*args):
#     for i in args:
#         if isinstance(i,int):
#             print(i)
#
# print(function_(10,2.3, "a", 4+2j, True, "python", "snake"))


"""WAF that takes multiple args and returns only the string in reversed order"""


# def function_(*args):
#     for i in args:
#         if isinstance(i,str):
#             print(i[::-1])
#
# print(function_(10,2.3, "a", 4+2j, True, "python", "snake"))


"""Variable keyword arguments(**kwargs)"""

"""WAF that returns no of positional arguments and no of keyword arguments"""


# def count_(*args, **kwargs):
#
# print(count_(1, 2, 3, a=10, b=29, c=30, d=34))


"""WAF that checks if the given args is greater than 5 or not"""

# def number_args(*args):
#     if len(args) > 5:
#          return "The arguments are greater than 5"
#
#     else:
#         return "THe number of args less than 5"
#
# print(number_args(1,2,3,4,5))

""" to print default message "Hi everyone" if there no user input else print the message given by the user"""

#
# def message(msg="Hi everyone"):
#     return msg
#
# print(message("hello"))


"""WAF to check whether the number is prime or not"""


# def prime_num(num):
#
#     for i in range(2, num):
#         if num % i == 0:
#             return f"{num} is not prime"
#         return f"{num} is a prime"
# #
# print(prime_num(11))

#
# def last_digit(num):
#      return num%10
#
# print(last_digit("123")

# def is_perfect_square(num):
#
#     for i in range(num):
#         if i**2 == num:
#             return True
#     return False
#
# print(is_perfect_square(27))



# def func( string , num):
#
#     if num == 0:
#         return string[1::2]
#     elif num == 1:
#         return string[::2]
#     else:
#         return "n value is invalid"
#
# print(func("TRACXN",2))



"""WAF to check if the given number is a fibonacci number"""

# def fib(num):
#
#     a = 0
#     b = 1
#     while a <= num:
#         if a == num:
#             return f"{num} is a fibonacci number"
#         c = a + b
#         a = b
#         b = c
#     return f"{num} is not a fibonacci number"
#
#
# print(fib(3))

"""WAF that takes variable number of inputs and return the length of all the iterables """
#
# def func(*args, **kwargs):
#
#     for item in args:
#         if not isinstance(item, (int, float, bool, complex)):
#             print (item, len(item))
#
#
# func(1, 2.3, "a", [1, 2, 3], (1, 2, 3, 4), "string")

#
# def func(*args):
#     print(*args)
#
#
# func()


































































