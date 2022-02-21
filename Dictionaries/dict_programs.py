""""WAP to create a dictionary to count the no of occurrances of characters"""


# string = "hello"

# d={}
#
# for char in string:
#     d[char] = string.count(char)
#
# print(d)


#without using any inbuilt method

# d = {}
#
# for item in string:
#     if item not in d:
#         d[item] = 1
#     else:
#         d[item] += 1
#
# print(d)

# from collections import defaultdict
# dd= defaultdict(int)
# for char in string:
#      dd[char] = dd[char]+1
#
# print(dd)

"""WAP to create a dictionary with word and its count pair"""

# s = "hello world how are you. This world is beautiful"
#
# words = s.split()
# d = {}
#
# for word in words:
#     if word not in d:
#         d[word] = 1
#     else:
#         d[word] += 1
# print(d)
#
# from collections import defaultdict
#
# dd= defaultdict(int)
#
# for word in words:
#     dd[word] += 1

# print(dd)

"""WAP to create a dictionary with word and its length pair"""

#
# s = "python is a language and python programming is fun"
#
# d = {}
#
#
# words = s.split()
#
# for word in words:
#     if word not in d:
#         d[word] = len(word)
#
# print(d)
#
# from collections import defaultdict
#
# dd = defaultdict(int)
#
# for word in words:
#     dd[word] = len(word)
#
# print(dd)

"""WAP to create a dictionary with word and its length pair only if the word is of even length"""

# s = "python is language and python programming is easy"
# d = {}
# words = s.split()
#
# for word in words:
#     if len(word) % 2 == 0:
#         d[word] = len(word)
#
# print(d)
#
# from collections import defaultdict
#
# dd= defaultdict(int)
#
# for word in words:
#     if len(word) % 2 == 0:
#         dd[word] = len(word)
#
# print(dd)








