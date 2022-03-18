'''program to check if the given number is even'''
#
# number = int(input("enter the number: "))
#
# if number % 2 == 0:
#     print(" The number is even")
# # else:
# #     if number % 2 != 0:
# #         print(" The number is not even")

'''To check if the given character is in lowercase'''
#
# char = input(" Enter the character: ")
#
# if "a" <= char <= "z":
#     print(" The given character is in lowercase")

""" To check if the given element is present in the collection"""
#
# list_ = ["python", "java", "linux", "ruby", "nodejs"]
# element = "java"
#
# if element in list_:
#     print("Element is present in the list")

t1 = ('rose', 'red', 'green')
t2 = (2, 3, 4, 5, 6)
# i = 0
# j = 0
# while j <= len(t2):
#     if j > i:
#
#     key = t1[i]
#     value = t2[j]
#     print(key, value)
#

temp1 = len(t1)
temp2 = len(t2)
d = {}
for i in range(temp2):
    print(t1[i % temp1], t2[i])



