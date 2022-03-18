path = r"C:\Users\Admin\PycharmProjects\Alpha_project3\files_directory\txt_log_files\sample.txt"
#
# with open(path) as file:
#     data = file.read()
#     print(data)

# with open(path) as file:
#     data = file.readlines()
#     print(data)
#     for line_no, line in enumerate(data):
#         print(line_no, line)

# with open(path) as file:
#     data = file.readline()
#     print(data)
#     print(file.readline())
#     print(file.readline())

# with open(path) as file:
#     print(file.readline(10))
#     print(file.readline(5))
#     print(file.readline())
#     print(file.readline())
#     print(file.readlines())

# with open(path) as file:
#     for line in file:
#         print(line)

"""count the number of lines in the file"""

# with open(path) as file:
#     count = 0
#     for line in file:
#         count += 1
#     print(count)

"""lineno and line in the file"""

with open(path) as file:
    for line_no, line in enumerate(file, start=1):
        print(line_no, line, sep="->")

















