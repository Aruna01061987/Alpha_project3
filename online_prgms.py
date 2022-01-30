#WAP to print tuple of characters and its ascii value by taking a string of your choice

# str_= "hello worl
#
# for i in str_:
#     print((i, ord(i)))
#
# n=11
#
# for i in range(2,n):
#     if n%i==0:
#         print("the number is not prime prime")
#     else:
#         print("the number is a prime number")
#
# str_="hello world#$$ 123yuiy"
# # sum=0
# # for i in str_:
# #     if i.isnumeric():
# #         sum=sum+int(i)
# # print(sum)
# count = 0
# for i in str_:
#     if i.isalpha():
#         if i.lower() not in 'aeiou':
#             count += 1
#             print(i, end=" ")
# print()
# print(count)

#
# str_= "python"
#
# # for index,item in enumerate(str_):
# #     print((index,item))

#
# for i in range(len(str_)):
#     print((i, str_[i]))

# str_ = "python the char"
#
# # # print(str_[::-1])
# # s = ""
# # for i in str_:
# #     s = i + s
# # print(s)
#
# for i in reversed(str_):
#     print(i, end='')

# str_ = "DFD^%^&&^9008fgfs"
#
# for i in str_:
#     if not i.isalnum():
#         print(i)
#
# # for i in str_:
# #     if i not ('a' <= i.lower() <= 'z') or 0 <= i <= 9:
# #         print(i)

str_ = "python the "

ch = input("enter the character:")
for i in range(0,len(str_)):
    if ch == str_[i]:
        print(i, str_[i])
    else:
        print(f"{ch} is not present")
