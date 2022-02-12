import csv

# path = r"C:\Users\Admin\PycharmProjects\Alpha_project3\files_directory\csv _files\employees.csv"

"""WAP to read  all the names of the employess in employess.csv file"""
# with open(path) as csv_file:
#     r_obj = csv.reader(csv_file)
#     for row in r_obj:
#         print(row[0])


"""WAP to print only the salaries that are>70000"""

# with open(path) as csv_file:
#     r_obj = csv.reader(csv_file)
#     next(r_obj)
#     for row in r_obj:
#         if int(row[3]) > 70000:
#             print(row[0], row[3])

"""WAP to group male and female employees"""

# from collections import defaultdict
# dd=defaultdict(list)
#
# with open(path) as csv_file:
#     r_obj = csv.reader(csv_file)
#     next(r_obj)
#     for row in r_obj:
#         if row[1] == 'male':
#             dd[row[1]] += [row[0]]
#         else:
#             dd[row[1]] += [row[0]]
# print(dd)

"""WAP to group employees based on their team"""

# from collections import defaultdict
# dd = defaultdict(list)
#
# with open(path) as csv_file:
#     r_obj = csv.reader(csv_file)
#     next(r_obj)
#     for row in r_obj:
#             dd[row[2]] += [row[0]]
# print(dd)


"""WAP to sort the shares in test.csv file based on the share prices"""

# path = r"C:\Users\Admin\PycharmProjects\Alpha_project3\files_directory\csv _files\test.csv"
#
# # with open(path) as file:
# #     read_obj = csv.DictReader(file)
# #     l = list(read_obj)
# #     res = sorted(l, key=lambda d: float(d[price]))
# #     print(list(res))
#
# with open(path) as file:
#     read_obj = csv.reader(file)
#     next(read_obj)
#     sum = 0
#     for row in read_obj:
#         sum += int(row[1])
# print(sum)


# def recursive_func(string):
#     print(string)
#     return recursive_func(string[1::])
#
# recursive_func("hai")
#
# #  import sys
# # sys.setrecursionlimit(10)
# # print(sys.getrecursionlimit())
# #
# # sys.getrecursionlimit()

import sys
print(sys.getrecursionlimit())
