"""Write a decorator that executes a function for 3 times"""

# def spam(func):
#     def wrapper(*args, **kwargs):
#         for i in range(0, 3):
#             res = func(*args, **kwargs)
#             print(res[::-1])
#     return wrapper
#
#
# @spam
# def reverse_(string):
#     return string
#
# reverse_("hello")

"""WA decorator which executes a function n times"""
#
# def p_outer(n):
#     def outer(func):
#         def wrapper(*args,**kwargs):
#             for i in range(n):
#                 func(*args,**kwargs)
#         return wrapper
#     return outer

"""WADF to count the number of arguments passed to a function"""

#
# def spam(func):
#     def wrapper(*args, **kwargs):
#         ccount = len(args) + len(kwargs)
#         print(ccount)
#         return func(*args, **kwargs)
#     return wrapper
#
# @spam #f1 = spam(f1)
# def f1(a):
#     return "In function"
#
#
# print(f1('kasi'))
#
#
# from time import sleep
#
#
# def delay(func):
#     def wrapper(*args, **kwargs):
#         sleep(5)
#         return func(*args, **kwargs)
#     return wrapper
#
#
# def reverse(func):
#     def wrapper(*args, **kwargs):
#         return func(*args, **kwargs)
#     return wrapper
#
# @delay
# def greet():
#     return "hello world"
#
# @delay
# def greeting(name):
#     return f"hello {name}"
#
# @delay
# def add(a, b):
#     return a+b
#
#
# print(add(1,2))

"""Decorator to validate the types of args passed by the user"""

#
# numbers = [1234567890, 9087654321, 911234567890, 119876543210]
#
#
# def add_prefix(number):
#     str_number = str(number)
#     if len(str_number) == 10:
#         str_number = "+91-" + str_number
#         return str_number
#     elif len(str_number) == 12 and str_number.startswith('91'):
#         str_number = "+"+ str_number[:2]+"-"+str_number[2:]
#         return str_number
#     else:
#         return str_number
#
#
# def prefix_country_code(func):
#     def wrapper(*args, **kwargs):
#         temp = args[0]
#         processed_numbers = [add_prefix(number) for number in temp]
#         return func(processed_numbers)
#     return wrapper
#
#
# @prefix_country_code
# def print_numbers(phone_numbers):
#     for item in phone_numbers:
#         print(item)
#
#
# print_numbers(numbers)

#################################   closures #################################

#
# from time import sleep
#
#
# def add(a, b):
#     name = "sandeep"
#
#     def wrapper():
#         print(name)
#         return a+b
#     return wrapper()
#
#
# def delay(seconds, func):
#     sleep(seconds)
#     return func
#
#
# a = add(1,2)
#
# print(delay(5,a))

####################################################################################


# def spam(func):
#     def wrapper():
#         print("In wrapper")
#         return func()
#     return wrapper
#
#
# @spam    #display = spam(display)
# def display():
#     print("Hi there")
#
#
# display()

"""WA decorator that logs a message before executing any function"""

#
# def log(func):
#     def wrapper(*args, **kwargs):
#         print("In log decorator function")
#         return func(*args, **kwargs)
#     return wrapper
#
#
# @log
# def add(a, b):
#     return a+b
#
#
# print(add(7, 8))


"""WA decorator to input some delay before executing any fn"""

#
# import time
#
#
# def delay(func):
#     def wrapper(*args, **kwargs):
#         time.sleep(2)
#         return func(*args, **kwargs)
#     return wrapper
#
#
# @delay
# def add_even(numbers):
#     for num in numbers:
#         if num % 2 == 0:
#             print(num)
#
#
# add_even([12, 23, 10, 43])

"""WA decorator which takes strings and reverses them"""


# def reverse(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         l = []
#         for word in res:
#             l.append(word[::-1])
#         print(l)
#     return wrapper
#
#
# @reverse
# def spam(*string):
#     return string
#
#
# spam("hello", "java", "python")

# def logging(msg="Hello world", debug=True):
#     def log(func):
#         def wrapper(*args, **kwargs):
#             if debug:
#                 print(msg, func.__name__, sep='\n')
#             return func(*args, **kwargs)
#         return wrapper
#     return log
#
#
# @logging("Hello python")
# def display():
#     return "hi there!"
#
#
# @logging()
# def add():
#     return "done"
#
#
# print(display())
# print(add())


# import time
#
#
# def _delay(time_delay):
#     def delay(func):
#         def wrapper(*args, **kwargs):
#             time.sleep(time_delay)
#             return func(*args, **kwargs)
#         return wrapper
#     return delay
#
#
# @_delay(2)
# def display():
#     return "Hi there, how are you?"
#
#
# print(display())

# def reverse(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         if isinstance(res, str):
#             return res[::-1]
#         return res
#     return wrapper
#
#
# @reverse
# def display():
#     return 768
#
#
# print(display())

# import time
#
#
# def _time(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         time.sleep(2)
#         res = func(*args, **kwargs)
#         end = time.time()
#         return f"The execution time for {func.__name__}: {end-start}"
#     return wrapper
#
#
# @_time
# def display():
#     print("DONE")
#
# print(display())


# def positive(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         return abs(res)
#     return wrapper
#
#
# @positive
# def mul(a, b):
#     return a*b
#
# print(mul(-9, 4))

# def cache(func):
#     _cache = {}
#
#     def wrapper(*args, **kwargs):
#         if args not in _cache:
#             res = func(*args, **kwargs)
#             _cache[args] = res
#             return res
#         print("returning cache's result")
#         return _cache[args]
#     return wrapper
#
#
# @cache
# def add(a, b):
#     return a+b
#
#
# print(add(3,4))
# print(add(4,5))
# print(add(3,4))

# def in_(func):
#     def c(*args, **kwargs):
#         print("some")
#         func(*args, **kwargs)
#         print("*some*")
#     return c
#
# @in_
# def inn_(func):
#     def c(*args, **kwargs):
#         print("more")
#         func(*args, **kwargs)
#         print("*more*")
#     return c
#
# @in_
# @inn_
# def d(a):
#     print(a)
#
#
# print(d("hello"))

# def calci(func):
#     func.count = 0
#     def wrapper(*args, **kwargs):
#         print(f"you called {func.__name__} function")
#         res = func(*args, **kwargs)
#         func.count += 1
#         print(f"you called {func.__name__} {func.count} times")
#         return res
#     return wrapper
#
#
# @calci
# def add(a, b):      #add = calci(add)
#     return a + b
#
#
# d = add(3,4)        #add = calci(add)
# print(d)


def log(func):
    def wrapper(*args, **kwargs):
        print("calling decorator")
        return func(*args, **kwargs)
    return wrapper


def logging(cls):
    for key, value in cls.__dict__.items():
        if callable(value):
            setattr(cls, key, log(value))
    return cls

@logging
class Arithmetic:
    def __init__(self, a, b):
        self.a = a
        self.b =b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a + self.b

    def mul(self):
        return self.a * self.b


a = Arithmetic(4, 5)

