#program to get the below output:
#['b', 'd']

# d = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
#
# keys = list(d.keys())
# print(keys[1::2])
#
#
# #Can we have multiple init methods in a class
#
# class Point:
#     def __init__(self, a, b):
#         self.a =a
#         self.b = b
#
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c

#Write decorator to prefix +91 to the original phone numbers

# numbers = [1234567890, 123456790, 1234567890]
#
#
# def prefix_country_code(func):
#     def wrapper(*args, **kwargs):
#         ph_numbers, = args
#         prefix_numbers = ["+91-"+str(number) for number in ph_numbers]
#         return func(prefix_numbers)
#     return wrapper
#
#
# @prefix_country_code
# def print_numbers(numbers):
#     for num in numbers:
#         print(num)
#
#
# p = print_numbers(numbers)
# print(p)

#In the list below, find all the number pairs which results in 10 either when added or subtracted

# a = [3, 5, -4, 8, 11, 1, -1, 6]
#
# for n1 in a:
#     for n2 in a:
#         if n1!= n2:
#             if n1+n2 == 10 or n1-n2 == 10:
#                 print((n1, n2))

#1. WAP to find the length of the string without using induilt function(len)

# string = "python"
#
# def _len(string):
#     count = 0
#     for char in string:
#         count += 1
#     return count
#
# print(_len(string))

#2. WAP to reverse a string without using any inbuilt functions

# string = "Hello"
#
# #using slicing
# _string = string[::-1]
# print(_string)
#
# #using for loop
#
# _str = ""
# for char in string:
#     _str = char+_str
#
# print(_str)

#3. WAP to replace one string with another e.g "HEllo world" replace "world" with "universe)

# s = "Hello world"
# print(s.replace("world", "universe"))

# l = s.split()
# l[1] = "universe"
# str_ = " ".join(l)
# print(str_)

#4. WAP to convert a string to a list and vice-versa

# def convert_to_string(any_list):
#     return " ".join(any_list)
#
# def convert_to_list(any_string):
#     return any_string.split()
#
# print(convert_to_string(["hello", "world"]))
# print(convert_to_list("python is a language"))

#5. Convert the string "Hello world welcome to python" to a comma separated string

# string = "Hello world welcome to python"
# str_ = ",".join(string.split())
# print(str_)

#6. WAP to print alternate characters in a string

# s = "hello world"
# print(s[::2])

#7. WAP to print ascii values of the characters present in a string

# s = "hello"
# for char in s:
#     print(f'{char}-->{ord(char)}')

#8. WAP to convert upper case to lower case and vice-versa without using inbuilt method

# s = "HeLLo"
# l = ""

#using swapcase
# print(s.swapcase())

#without swapcase

# for c in s:
#     if c.islower():
#         l += chr(ord(c) - 32)
#     elif c.isupper():
#         l += chr(ord(c) + 32)
#     else:
#         l += c

# print(l)

# def swap_case(string):
#     str_ = ""
#     for c in s:
#         if ord(c) >= 97 and ord(c) <= 122:
#             str_ += chr(ord(c)-32)
#         elif ord(c) >= 65 and ord(c) <= 90:
#             str_ += chr(ord(c)+32)
#         else:
#             str_ += c
#     return str_
#
# print(swap_case(s))

#9. WAP to swap two numbers without using 3rd variable

# a = 10
# b = 20
#
# b, a = a, b
# print(a)
# print(b)

#10. WAP to merge two different lists

# a = (1, 2, 3)
# b = {'a': 4, 'b': 5, 'c': 6}
#
# # c = a + b
# # print(c)
# #
# # d = [*a, *b]
# # print(d)
#
# from itertools import chain
#
# s = chain(a, b)
# print(tuple(s))

#WAP to read a random line in a file.(ex. 50, 65, 78 line)

# from itertools import islice
# with open(r"C:\Users\Admin\PycharmProjects\Alpha_project3\files_directory\txt_log_files\sample.txt") as file:
#     line = islice(file, 5, 6)
#     print(list(line))
    # for i in line:
    #     print(i)


# def read_random_line(lineno):
#     file = open(r"C:\Users\Admin\PycharmProjects\Alpha_project3\files_directory\txt_log_files\sample.txt")
#     for index,line in enumerate(file, start=1):
#         if index == lineno:
#             return line

# def read_random_line(start_line, end_line):
#     with open(r"C:\Users\Admin\PycharmProjects\Alpha_project3\files_directory\txt_log_files\sample.txt") as enumerate(file, start=1):
#         if index in range(start_line, end_line):
#             print(line)
#
# read_random_line(10, 15)

#WAP to print last N lines of a file

# from itertools import islice
#
#
# def last_n_lines(n):
#     count = 0
#     with open(r"C:\Users\Admin\PycharmProjects\Alpha_project3\files_directory\txt_log_files\sample.txt") as f:
#         for line in f:
#             count += 1
#         f.seek(0)
#         lines = islice(f, count-n, None)
#         return list(lines)
#
#
# print(last_n_lines(5))


# using dqueue


# from collections import deque
#
#
# def last(n):
#     with open(r"C:\Users\Admin\PycharmProjects\Alpha_project3\files_directory\txt_log_files\sample.txt") as file:
#         d = deque(file,n)
#         return d
#
#
# last_lines = last(5)
#
# for line in last_lines:
#     print(line)

#WAP to check if the given string is a plaindrome or not without using reversed method


# def is_palindrome(string):
#
#     rev_string = string[::-1]
#
#     if string == rev_string:
#         return f"palindrome"
#     else:
#         return f"not a palindrome"
#
# print(is_palindrome("madam"))
#
# print(is_palindrome("chopper"))

#WAP to check for a character in a given string and return the corresponding index

# def char_index(str_, c):
#     for index, char in enumerate(str_):
#         if c == char:
#             print(index)
#
#
# char_index("python", 'h')


# def search(string, key):
#     try:
#         return string.index(key)
#     except ValueError:
#         return "Key not found"
#
#
# print(search("hello", "l"))

#WAP to get the below output

# sentence = "hello world welcome to python programming hi there"
# # d = {'h': ['hello', 'hi'], 'w': ['world', 'welcome'], 't': ['to', 'there']}
#
# from collections import defaultdict
#
# d = defaultdict(list)
# words = sentence.split()

# for word in words:
#     d[word[0]] += [word]
#
# print(d)

# for word in words:
#     d[word[0]].append(word)
#
# print(d)


# #WAP to replace all the characters with - if the character occurs more than once in a string
# def replace_str(my_string):
#     new_string = []
#     for char in my_string:
#         if my_string.count(char) > 1:
#             new_string.append("-")
#         else:
#             new_string.append(char)
#     return "".join(new_string)
#
#
# print(replace_str("hellohai"))

#WA decorator that returns only positive values of the subtraction

# def positive(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return abs(result)
#     return wrapper
#
# @positive
# def sub(a, b):
#     return a-b
#
#
# print(sub(1, 2))
# print(sub(-1, 100))
# print(sub(-100, 1))

#How to get the number of instances of a class that has been created
#
#
# class Demo:
#     count = 0
#
#     def __init__(self):
#         Demo.count += 1
#
#
# d1 = Demo()
# d2 = Demo()
#
# print(Demo.count)

#WAF which takes a list of strings and integers. If the item is a string it should print as is and if the item
#is integer or float it should reverse it


# def rev_non_str(_list):
#     l1 = []
#     for i in _list:
#         if isinstance(i, str):
#             l1.append(i)
#         elif isinstance(i, (float, int)):
#             l1.append(str(i)[::-1])
#     return l1
#
#
# l = ['dad', 'mom', 3.24, 1233]
# print(rev_non_str(l))

# #WA class named Simple and it should have iteration capability
#
# class Simple:
#     def __init__(self, _list):
#         self._list = _list
#
#     def __iter__(self):
#         return iter(self._list)
#
#
# l = [1, 2, 3, 'a', 'n']
#
# s = Simple(l)
#
# for item in s:
#     print(item)

#WA custom class which can access the values of dictionaries using d['a'] and d.a
#
# class MyDict:
#     def __init__(self, dd):
#         self.dd = dd
#
#     def __getitem__(self, item):
#         return self.dd[item]
#
#     def __getattr__(self, item):
#         return self.dd[item]
#
#
# d = MyDict({'a': 1, 'b': 2})
# print(d.a)
# print(d['b'])

# class MyDict:
#     def __init__(self, d):
#         self.__dict__.update(d)
#
#     def __getitem__(self, item):
#         return self.__dict__[item]
#
#
# d = MyDict({'a': 1, 'b': 2})
# print(d.a)
# print(d['b'])

#WAP to get the below output

# sentence = "Hi How are you"
#output: iH woH era ouy

# l = sentence.split()
#
# l1 = [word[::-1] for word in l]
#
# print(" ".join(l1))
#
# #WAP to get the below output
#
# sentence = "Hi How are you"
# #output: "uoy era woH iH"
#
# print(sentence[::-1])

#How to remove duplicates from the list without using inbuilt functions

# items = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
#
# print(list(set(items)))
#
# unique = []
#
# for item in items:
#     if item not in unique:
#         unique.append(item)
#
# print(unique)

#WAP to find the longest word in the sentence

# sentence = "Hello world Welcome to python"
#
# words = sentence.split()
#
# longest = sorted(words, key=lambda item: len(item))
#
# print(longest[-1])
#
# d = {word: len(word) for word in words}
# print(max(d.items(), key=lambda item: item[-1]))

#WAP to reverse the values in the dictionary if the value is of type Stirng

# d = {'a': 'hello', 'b': 100, 'c': 10.1, 'd': 'dlrow'}
#
# rev = {key: value[::-1] if isinstance(value, str) else value for key, value in d.items()}
# print(rev)

#WAP to get 1234

# t = ('1', '2', '3', '4')
# print("".join(t))

#How to get the elements that are in list b but not in list a

a = [1, 2, 3]
b = [1, 2, 3, 4]

set_a = set(a)
set_b = set(b)

print(set_b.difference(set_a))

for item in b:
    if item not in a:
        print(item)

#A function takes variable number of positional arguments as input. How to check if the arguments that are passed are more than 5






def func(a, key=0):
    if key == 0:
        return a[1::2]
    else:
        return a[::2]

print(func("TRACXN"))







