# To traverse through the list and create list comprehension

# l = ["python", 10, 3.2, "selenium", "Java"]
#
# nl = [item for item in l]
#
# print(nl)

#########################################################

""" print index and its corresponding item in the list """

# l = ["python", 10, 3.2, "selenium", "Java"]
#
# new_list = [item for item in enumerate(l)]
#
# print(new_list)

########################################################

""" traversing through a list in reversed order """
# l = ["python", 10, 3.2, "selenium", "Java"]
#
# new_list = [item for item in l[::-1]]
#
# print(new_list)
#
# new_list1 = [item for item in reversed(l)]
#
# print(new_list1)
#
# new_list2 = [l[item] for item in range(len(l)-1, -1, -1)]
#
# print(new_list2)
########################################################

""" print even indexed elements in the list """

#enumerate

# l = ["python", 10, 3.2, "selenium", "Java"]
#
# new_list = [item for index,item in enumerate(l) if index % 2 == 0]
#
# print(new_list)
#
# #range
#
# new_list1 = [l[item] for item in range(0, len(l), 2)]
#
# print(new_list1)
#
# #slicing
#
# new_list2 = [item for item in l[::2]]
#
# print(new_list2)

#####################################################################

""" print integers in a list """

l = ["python", 10, 3.2, "selenium", "Java"]

new_list = [item for item in l if isinstance(item, int)]

print(new_list)


