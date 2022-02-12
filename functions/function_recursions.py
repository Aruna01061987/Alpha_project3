"""WAP to print numbers till 10"""


# # def count_(n):
#     if n > 10:
#         return
#     print(n)
#     count_(n + 1)


# count_(10,1)

# def add_digit(num):
#     count=0
#     for i in str(num):
#         count += int(i)
#     return count
#
# print(add_digit(234))


"""To print the sum of digits in a number"""

# num = 123
# sum = 0
# while num > 0:
#     last = num % 10
#     sum += last
#     num = num // 10
#
# # using recursion

# sum_ = 0
# for i in range(5):
#     sum_ += i
#
# print(sum_)

# def fact_(n, sum=1):
#     if n > 1:
#         sum *= n
#         return fact_(n-1, sum)

"""Write a recursion program to count """
#
# def count_digits(num, count=0):
#     # if num > 0:
#         num = num // 10
#         count += 1
#         return count_digits(num, count)
#     # return count
#
#
# print(count_digits(1234))

"""program to reverse a program using recursions"""

# def reverse_sting(string, i=0, a = ""):


# def fibonacci(n):
#     if n < 0:
#         print("invalid input")
#     elif n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return (fibonacci(n-1)+ fibonacci(n-2))
#
# for i in range(n):
#     print(fibonacci(i), end= " ")














