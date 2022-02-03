""" 1 to 10 """

# def numbers(start,end):
#     for num in range(start,end+1):
#         print(num)
#
#
# print(numbers(1,10))

""" 10 to 1 """

# def numbers(end, start):
#     for num in range(end, start-1, -1):
#         print(num)
#
#
# numbers(10, 1)

""" -10 to -1 """

# def numbers(start, end):
#     for num in range(start, end):
#         print(num)
#
# numbers(-10, 0)


""" even numbers  from 1 to 10 """

# def even_numbers(start, end):
#     for num in range(start, end+1):
#         if num % 2 == 0:
#             print(num)
#
# even_numbers(1,10)


""" traversing through strings """

# def string_(str_):
#     for char in str_:
#         print(char, end=" ")
#
# string_("python")


""" traversing through lists """


# def list_(lst):
#     for item in lst:
#         print(item)
#
#     # for index in range(len(lst)):
#     #     print(lst[index])
#
#
# l = [10,20,30,40]
# list_(l)


""" traversing through sets """
# set_ = {"hai", "hello", "how", "are", "you"}


# def traverse_set(set_):
#
#     for item in set_:
#         print(item)
#
#
# set_ = {"hai", "hello", "how", "are", "you"}
# traverse_set(set_)

""" traversing through dictionaries """
#
# def traverse_dict(dict_):
#
#     for key in dict_:
#         print(key, dict_[key])
#
#
# d = {"one": 1, "two": 2, "three": 3}
# traverse_dict(d)


""" to print index and character in a string """

# def string(str_):
#
#     for i in range(len(str_)):
#         print(i, str_[i])
#
#
# string("python")

""" traversing a string in reversed order """

# def rev_string(str_):
#
#     for i in reversed(str_):
#         print(i)
#
#     for i in range(len(str_)-1, -1, -1):
#         print(str_[i])
#
#     for i in str_[::-1]:
#         print(i)
#
#
# rev_string("python")

""" count the number of characters in a string """

# def num_char(str_):
#     count = 0
#     for i in str_:
#         count += 1
#     print(count)
#
#     print(len(str_))
#
#
# num_char("python")

""" print even indexed characters in the string """

# def even_indexed_char(str_):
#
#     # for i in range(len(str_)):
#     #     if i % 2 == 0:
#     #         print(str_[i])
#
#     # for i in str_[::2]:
#     #     print(i)
#
#     for i in range(0, len(str_), 2):
#         print(str_[i])
#
#
# even_indexed_char("hello world")








# string = "hello world"


