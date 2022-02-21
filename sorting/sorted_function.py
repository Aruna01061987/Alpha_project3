"""WAP to sort a dict based on keys last item"""

# d = {"gmail": 5, "walmart":7, "apple":3, "flipkart":8}
#
# print(sorted(d.items(), key=lambda item: item[0][-1]))
#
# # print(sorted(d.items(), key= lambda item: item[1]))
#
# print(sorted(d.values()))
#
# """WAP to print the longest non repeated word in the given sentence"""
#
# sentence ='hi how are you how is your health health your language'
#
# words = sentence.split()
#
# d_len = {word: len(word) for word in words if words.count(word) == 1}
#
# res = sorted(d_len.items(), key= lambda item: item[-1])
#
# print(res[-1])


"""sort the below list based on names, class, age"""

# l = [{"name": "Ram", "class": 6, "age": 12},
#      {"name": "Shyam", "class": 12, "age": 18},
#      {"name": "JOhn", "class": 8, "age": 13}]
#
# print(sorted(l, key=lambda item: item['name']))


# s = "hello"
# print(sorted(s))
#
# l = [5, 4, 8, 6, 1, 9, 11, 7]
# print(sorted(l))

# l = [(1, 5, 6), (1, 2, 3), (2, 4, 3) ]
# print(sorted(l))

# l = [[3, 'key'], [1, 'a'], [2, 'in']]
# print(sorted(l))

# set_ = {3, 9, 10, 4, 1, 5}
# print(sorted(set_))
#
# dict_ = {'gmail': 5, 'apple': 6, 'walmart': 8, 'flipkart': 9}
# print(sorted(dict_))

# l = ["python", "java", "c", "ruby", "perl"]
# print(sorted(l, key=len))

# l = ["python", "java", "c", "ruby", "perl"]
# print(sorted(l, key=len, reverse=True))

# sentence = "python is a programming language"
#
# words = sentence.split()
#
# shortest, *rest, longest = sorted(words, key=len)
# print(f"shortest is '{shortest}', longest is '{longest}'")

# list_ = sorted(words, key=len)
# print(list_[0], list_[-1])
#
# sentence = "python is a programming language"
# words = sentence.split()
# shortest, *rest, longest = sorted(words, key=len)
# print((shortest, len(shortest), longest, len(longest)))

# l = ["python", "java", "c", "ruby", "perl"]
# print(sorted(l, key= lambda item: item[-1]))

# def last_item(ele):
#      return ele[-1]
#
# print(sorted(l, key= last_item))

# print(sorted(l, key=lambda item: item[-1]))
#
# res = lambda n1, n2: n1*n2
# print(res(3,4))

# res = lambda string_: string_[-1]
# print(res("hello"))
#
# palindrome = lambda string_: string_ if string_ == string_[::-1] else "not a palindrome"
#
# print(palindrome("mom"))


# l = ["python", "java", "c", "ruby", "perl"]
#
# print(sorted(l, key= lambda item: item[-1]))

#
# d = {"gmail": 5, "walmart": 4, "flipkart": 6}

# print(sorted(d))
# print(sorted(d.keys()))
# print(sorted(d.items()))

# print(sorted(d.items(), key= lambda item: item[1]))
#
# print(d.items())

# sentence = "hi how are you how is your health"
#
# list_= sentence.split()

# d_count = {word:list_.count(word) for word in list_}
# print(d_count)
#
# res = (sorted(d_count.items(), key = lambda item: item[-1]))
#
# print(res[-1])

# d_len = {word: len(word) for word in list_ if list_.count(word) == 1}
# res = sorted(d_len.items(), key= lambda item: item[1])
# print(res[-1])

"""WA function that accepts two string as input and checks if they are anagrams"""

#
# def is_anagram(str1, str2):
#
#     if len(str1) == len(str2):
#         for char in str1:
#             if char in str2:
#                 return True
#     else:
#         return False
#
#
# print(is_anagram('listen', 'silent'))


"""WAP to find the longest non-repeated word from the sentence"""


# sentence = "python is programming  language and programming is fun"
#
# words = sentence.split()
#
# d = {word: len(word) for word in words if words.count(word) == 1}
#
# res = sorted(d.items(), key=lambda item: item[1])
#
# print(res[-1])

"""WAP to to sort the list based on the first character of the word"""

# l = ["python", "apple", "language", "c++", "java"]
#
#
# print(sorted(l))
#
# # print(sorted(l, key=lambda word: word[0]))

"""WAP to sort the list based on the last character of the word"""


# l = ["python", "apple", "language", "c++", "java"]

# print(sorted(l, reverse=True))
#
# print(sorted(l, key=lambda word: word[-1]))

# word = "python"
# print(word[-1])














































