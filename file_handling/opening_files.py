from collections import Counter
"""WAP to count the number of """

path =r"C:\Users\Admin\PycharmProjects\Alpha_project3\files_directory\txt_log_files\sample.log"

# with open(path) as file:
#     count = 0
#     for line in file:
#         count += 1
#         print(count, line)

# with open(path) as file:
#     count = 0
#     for line in file:
#         words = line.split()
#         for word in words:
#             count += 1
#     print(count)

"""WAP to print the lines from the last of the file last line should be first"""

# with open(path) as file:
#     for line in reversed(list(file)):
#         print(line)


"""WAP to count the no of spaces in the given file"""


# with open(path) as file:
#     count = 0
#     for line in file:
#         n = line.count(' ')
#         count = count + n
#     print(count)

"""WAP to count the number of words starting with vowels in a file"""

# with open(path) as file:
#     count = 0
#     for line in file:
#         words = line.split()
#         for word in words:
#             if word[0].lower() in 'aeiou':
#                 count += 1
#     print(count)

"""WAP to create a dictionary of word and its count pair in the given dictionary"""
# from collections import defaultdict
# dd = defaultdict(int)
# with open(path) as file:
#     for line in file:
#         words = line.split()
#         for word in words:
#             dd[word] += 1
#     print(dd)

"""WAP to print all the ip address in the access-log.txt file"""

# with open(path) as file:
#     list_ = []
#     for line in file:
#         words = line.split()
#         list_.append(words[0])
# ip_ = Counter(list_)
# print(ip_.most_common())

"""WAP to create a dictionary of ip addresses and its count"""
#
# from collections import defaultdict
# dd = defaultdict(int)
# with open(path) as file:
#     for line in file:
#         if line.strip():
#             words = line.split()
#             dd[words[0]] += words.count(words[0])
#     print(dd)

"""WAP to print nth line in a file"""
#
# from itertools import islice
# # n=3
# # with open(path) as file:
# #     for line_no, line in enumerate(file, start = 1):
# #         if line_no <= n:
# #             print(line)
#
# n=2
# with open(path) as file:
#     count = 0
#     for line in file:
#         count += 1
#     file.seek(0)
#     res = islice(file, count-n, count)
#     print(list(res))

# from collections import defaultdict
# dd = defaultdict(int)
with open(path) as file:
    for line_no,line in enumerate(file):
        print(f"{line_no} length is {len(line)}")
        # if line.strip():
        #     list_ = line.split()
        #     print(list_[2])


















