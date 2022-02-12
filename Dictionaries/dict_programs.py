""""WAP to create a dictionary to count the no of occurrances of characters"""


string = "hello"

# d={}
#
# for char in string:
#     d[char] = string.count(char)
#
# print(d)


#without using any inbuilt method

d = {}

for item in string:
    if item not in d:
        d[item] = 1
    else:
        d[item] += 1

print(d)

# from collections import defaultdict
# dd= defaultdict(int)
# for char in string:
#      dd[char] = dd[char]+1
#
# print(dd)






