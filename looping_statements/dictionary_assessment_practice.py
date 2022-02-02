"""WAP to print only values from the dictionary"""

d = {'a': 1, "b": 2, "c": 3, "d": 4, "e":5}

# for key in d:
#     print(d[key], end=" ")
#     print()
#
# for key in d:
#     print(d.get(key), end=" ")
#     print()
# for value in d.values():
#     print(value, end="")
#     print()

# for key, value in d.items():
#     print(value, end=" ")
#     print()



"""print the items in a dictionary along with indices"""

# dict_ = {'a':1, 'b':2, 'c':3, 'd':4}
#
# for item in enumerate(dict_):
#     print(item,end="")
#
# for key, value in d.items():
#     print(key,value)

# for index,(key,value) in enumerate(d.items()):
#     print(index,key,value)

"""WAP to create a dict with a character and its count pair in a string"""

string = "hello world"
# d={}
# # for char in string:
# #     d[char] = string.count(char)
# # print(d)
# d={}
# for char in set(string):
#     d[char] = string.count(char)
# print(d)

d={}

for i in string:
    count = 0
    for j in string:
        if i == j:
            count += 1
    d[i] = count
print(d)

