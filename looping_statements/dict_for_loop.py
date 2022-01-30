#WAP to print the items in adictionary along with indices

# WAp to create a dictionary with character and its count in a string

# string = "hello world"
# d={}
#
# for i in set(string):
#     count=0
#     for j in string:
#         if i==j:
#             count+=1
#     d[i]=count
# print(d)

# s='hello'
# d={}
# for char in set(s):
#     if char


#WAP to create a dictionary with word and its count pair

#s="python is language, python programming is easy"
# a = s.split(" ")
# d={}
# for word in a:
#     d[word] = a.count(word)
# print(d)
#
# s="python is language, python programming is easy"
# d={}
# a=s.split(" ")
# for i in a:
#     count=0
#     for j in a:
#         if i == j:
#             count+=1
#         d[i] = count
# print(d)

#without using inbuilt method
# s="python is language, python"
#
# d={}
# a=s.split(' ')
# for word in a:
#     if word not in d:
#         d[word] = 1
#     else:
#         d[word] += 1
# print(d)

#using default dict
# from collections import defaultdict
# s="python is language, python programming is easy"
# a=s.split()
# dd=defaultdict(int)
#
# for word in a:
#     dd[word] = dd[word]+1
# print(dd)

#WAP to create a dictionary with word and its length pair

# s="python is language, python programming is easy"
# a= s.split()
# d = {}
# for word in a:
#     d[word] = len(word)
#
# print(d)

#WAP to create a dict with word and its length pair only if the word is of even length***********

# s="python is language, python programming is easy"
# a= s.split()
# d = {}
# for word in a:
#     if len(word)%2==0:
#         d[word] = len(word)
#
# print(d)

#WAP to create a dict with word and its length pair only if the word is starting with vowel

# s="python is language, on ogramming is easy"
# a= s.split()
# d = {}
# for word in a:
#     if word[0] in 'aeiouAEIOU':
#         d[word] = len(word)
#
# print(d)

#using default dict

# from collections import defaultdict
# dd= defaultdict(int)
# s="python is language, on ogramming is easy"
# a= s.split()
# for word in a:
#     if word[0] in 'aeiouAEIOU':
#         dd[word] = len(word)
#
# print(dd)
#WAP to create a dict with word and its count only if the word is not repeated

# s="python is language, python ogramming is easy"
# a= s.split()
# d = {}
# for word in a:
#     if a.count(word) == 1:
#         d[word] = a.count(word)
#
# print(d)

#WAP to reverse tthe values in the dictionary if the values is of type string
#d={"a":"hello", "b":100,"c":10.2,"d":"word"}

#WAP to get the following o/p

# sentence= "hello world welcome to python programming hi there"
# # op={'h': ["hello", "hi"], 'w': ["world","welcome"], 't' :["to","there"]}
# from collections import defaultdict
#
# dd= defaultdict(list)
#
# list_=sentence.split()
#
# for word in list_:
#     if word[0] not in dd:
#         dd[word[0]] = [word]
#     else:
#         dd[word[0]]+= [word]
# print(dd)

# names=["apple","google","gmail","yahoo","gmail","apple","gmail","google"]
# d={}
#
# for index, value in enumerate(names):
#     if value not in d:
#         d[value]= [index]
#     else:
#         d[value].append(index)
# print(d)

# from collections import defaultdict
# dd= defaultdict(list)
#
# names = ["apple", "google", "gmail", "yahoo", "gmail", "apple", "gmail", "google"]
#
# for index,value in enumerate(names):
#         dd[value]+= [index]
#
# print(dd)

#WAP to flip key and values

d={"a":1, "b":2, }