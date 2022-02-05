"""WAP to remove all the duplicates"""

# names = ['apple', 'google', 'apple', 'yahoo', 'google']
# new_names = set(names)
# print(new_names)

"""WAP to print all numeric values in alist"""

# items = ['apple', 1.2, 'google', '12.6', 26, '100']
#
# for item in items:
#     if isinstance(item, (int, float, complex)):
#         print(item)

"""WAP to sum all even numbers in the given string"""

# sentence = "hello 123 world 567 welcome to 9724 python"
# even_sum = 0
#
# for char in sentence:
#     if "0" <= char <= "9" and int(char) % 2 == 0:
#         even_sum += int(char)
#
# print(even_sum)

# sum = 0
# for i in sentence:
#     if i.isdigit():
#         if int(i) % 2 == 0:
#             sum += int(i)
# print(sum)

"""WAP to create a set with all the languages which starts with 'p' """

# languages =['python', 'java', 'perl', 'PHP', 'python', 'js node']

# s = set()
# for language in languages:
#     if language[0] in 'Pp':
#         s.add(language)
#
# print(s)

"""Build a list with only even length string"""

# names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']
#
# list_ = []
#
# for name in names:
#     if len(name) % 2 == 0:
#         list_.append(name)
#
# print(list_)


"""Reverse the item of a list if the item is of odd length string otherwise keep the item as is"""

# names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'c++', "SQL"]
#
# for name in names:
#     if len(name) % 2 != 0:
#         print(name[::-1])
#     else:
#         print(name)

"""WAP to print the sum of entire list and sum of only internal list"""

# l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# entire_sum = 0
# for item in l:
#     internal_sum = 0
#     for i in item:
#         internal_sum += i
#         entire_sum += i
#
#     print(internal_sum)
# print(entire_sum)

"""WAP to print list of prime numbers between 1-100"""

for i in range(100):
    if i > 1:
        for j in range(1,100):
            if i % j == 0:
                break
        else:
            print(i)





