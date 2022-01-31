"""" to traverse through a list"""


"""To create a list of tuples which is having index and its corresponding item"""
# using comprehension

# l = [1, 2, 3, 3]
#
# nl = [item for item in enumerate(l)]
#
# print(nl)

#normal method

# l = [1, 2, 3, 4]
#
# nl = []
#
# for item in enumerate(l):
#     nl.append(item)
#
# print(nl)

#using comprehensions

# l = [1, 2, 3, 4]
#
# nl = []
#
# for i in l:
#     if i % 2 == 0:
#         nl.append(i)
#
# print(nl)

""" To crete to list of odd and even numbers in seperate list using comprehensions"""

# l = list(range(10))
#
# evens = [for ]





# """To create a list using the following list, if the word is of even"""
#
# list_ = ["jave", "python", 10, True, 1.4, "c++", "ruby"]
#
# res = [item if isinstance(item, str) else (str(item)[::-1]) for item in list_]
#
# print(res)


files = ["Amazon", "flipkart", "walmart", "gmail", "yahoo"]

nfile = [word for word in files if word[0].lower() in "aeiou"]

print(nfile)