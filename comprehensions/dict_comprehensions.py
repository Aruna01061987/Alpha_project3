# """WAP to create a dict with char and its count pair"""
#
# string = "hello world"
# d = {}
#
# for char in string:
#     d[char] = string.count(char)
#
# print(d)
#
# # comprehension
#
# dict_ = {char: string.count(char) for char in string}
#
# print(dict_)
#
# """WAP to create a dict with word and its count pair"""
#
# sentence = "python is programming language"
# d = {}
#
# words = sentence.split()
#
# for word in words:
#     d[word] = sentence.count(word)
#
# print(d)
#
# # comprehension
#
# dict_ = {word: sentence.count(word) for word in words}
#
# print(dict_)

"""WAP to create a dict with word and its count pair only if the word is of even length"""

# sentence = "python is programming language"
# d = {}
#
# words = sentence.split()
#
# for word in words:
#     if len(word) % 2 == 0:
#         d[word] = words.count(word)
# print(d)
#
# #comprehension
#
# dict_ = {word: words.count(word) for word in words if len(word) % 2 == 0}
#
# print(dict_)

"""WAP to create a dict with index and word pair only if the word is of odd length reverse else print as it is"""

# sentence = "python is programming language"
#
# words = sentence.split()
# d = {}
#
# for index, item in enumerate(words):
#     if len(item) % 2 == 0:
#         d[index] = item
#
#     else:
#         d[index] = item[::-1]
# print(d)
#
# #comprehension
#
# dict_ = {index: word if len(word) % 2 == 0 else word[::-1] for index, word in enumerate(words)}
#
# print(dict_)

"""WAP to create a dict with word and its length pair only if the word is starting with vowel """

# sentence = "python is programming language"
#
# words = sentence.split()
#
#
# dict_ = {word: len(word) for word in words if word[0].lower() in "aeiou"}
# print(dict_)

"""create a dictionary of index and its item pair if the item is of string data type reverse it"""
#
# l = ["python", 10, 23.4, "there", True]
#
# dict_ = {index: item[::-1] if isinstance(item, str) else item for index, item in enumerate(l)}
#
# print(dict_)

"""create a dictionary of index and its word pair if the word is of type string keep it as it is else reverse it"""

# l = ["python", "there", [1,2,3], 19.9, 14+0j, "c++"]
#
# # dict_ = {index: item[::-1] if not isinstance(item, str) else item for index, item in enumerate(l)}
# #
# # print(dict_)
#
#
# dict_ = {index: item if isinstance(item, str) else str(item)[::-1] for index,item in enumerate(l)}
# print(dict_)

"""write a comprehension to flip keys and values in a dictionary"""

d= {"a": 1, "b": 2, "c":3, "d":4}
# dict_ = {value: key for key,value in d.items()}
# print(dict_)

dict_ = {d[key]: key for key in d}

print(dict_)

"""WAP to create a dictionary of character and its ascii value pair"""

# string = "python"
#
# dict_ = {char: ord(char) for char in string}
#
# print(dict_)

"""WAP to create a dictionary of"""
