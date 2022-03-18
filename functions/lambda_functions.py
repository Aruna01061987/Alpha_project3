
# #
# # res = lambda str_: str_[-1]
# #
# # print(res([1, 2, 3, 4]))
# #
# res = lambda str_: str_ == str_[::-1]
# print(res("madam"))
#
# # even_odd = lambda num: f"{num} is even" if num%2 == 0 else f"{num} is odd"
# #
# # print(even_odd(13))
#
# t = (22, )

list_ = ["mom", "dad"]
palindrome = lambda string: string == string[::-1]
print(palindrome(list_))



# a = map(lambda x: x % 2 == 0, [1, 2, 3, 4])
# print(list(a))


# a = map(lambda x: x % 2 == 0, [1, 2, 3, 4])
# print(list(a))
#
# a = lambda x: x*2
# print(a((1, 2)))
#
# a = map(lambda x: x % 2 == 0,[1, 2, 3, 4])

#
# n = lambda x, y: x*y
# res = n(1,2)

# l=[]
#
# b = [1,2,3,4,5]
# print(b)

# x= list()
# x.append(2)
# print(x)



# l = [2]
#
# print(l)




###########################################   practice  #######################################

""" square of a number """

# def squares(num):
#     return num ** 2

# squares = lambda num: num **2
#
# print(squares(3))

# res = squares(2)
# # print(res)
# # lambda args: expression
#
# # squares = lambda num: num ** 2
# # res = squares(2, )
# # print(res)
#
# """ even or not """
# evens = lambda num: num % 2 == 0
# # print(evens(5))
#
# if_even = lambda num: num % 2 ==0
# print(if_even(8))


# """ multiply 2 numbers """
# multiples = lambda num1, num2: num1 * num2
# # print(multiples(3, 6))

# product = lambda n1,n2: n1*n2
# print(product(12,45))

# last = lambda ele: ele[-1]
#
# print(last("hello"))
# print(last((1,2,[1,2,3])))





# """ last element of the sequence """
# last = lambda sequence: sequence[-1]
# # print(last("hello"))
# # print(last(("1", 2)))
#
# """ palindrome or not """
# palindrome = lambda string: f"{string} is a palindrome" if string == string[::-1] else "not a palindrome"
# # print(palindrome("mom"))
#
# """ even or odd """
# even_odd = lambda num: f"{num} is even" if num % 2 == 0 else f"{num} is odd"
# # print(even_odd(1))


"""WAP to get a list of tuples with character and iys ascii value pair"""


# word = "python"
#
#
# def ascii_(ch):
#     return ch, ord(ch)
#
#
# res = map(ascii_, word)
# print(list(res))














