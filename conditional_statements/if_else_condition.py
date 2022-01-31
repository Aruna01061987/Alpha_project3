""" To check if the given number is odd or even """

# number = 15
#
# if number % 2 == 0:
#     print(f"The number {number} is even")
# else:
#     print(f" The number {number} is odd ")

""" To check if the character is lower or uppercase """

# char = "#"
#
# if "a" <= char <= "z":
#     print(f" The character {char} is in lowercase")
# else:
#     if "A" <= char <= "Z":
#         print(f" The character {char} is in uppercase")
#     else:
#         print(" The given character is not an alphabet")

#using elif

# char = "n"
#
# if "a" <= char <= "z":
#     print(f" The character {char} is in lowercase")
# elif "A" <= char <= "Z":
#     print(f"The character {char} is in uppercase")
# else:
#     print(" The character is not an alpahbet")

#using built-in methods

# char = "9"
#
# if char.islower():
#     print(f"The character {char} is in lowercase")
#
# elif char.isupper():
#     print(f" The character {char} is in uppercase")
#
# else:
#     print(f" The character {char} is not an alphabet")

""" To check if given iterable is empty or not"""

# iterable = " "
#
# if len(iterable) != 0:
#     print(f"The given iterable is not empty")
#
# else:
#     print("THe given iterable is empty")

# using bool

# iterable = ""
#
# if bool(iterable):
#     print(" The iterable is not empty")
# else:
#     print(" The iterable is empty")

# without using bool
#
# iterable = "jack"
#
# if iterable:
#     print("The iterable is not empty")
#
# else:
#     print("The iterable is empty")

""" To check if the given value is default or non default """
#
# value = [1, 2]
#
# if value:
#     print("Given value is not default value")
#
# else:
#     print("It is a default value")

""" To convert lowercase to uppercase and vice-versa """

# char = "%"
#
# if "a" <= char <= "z":
#     print(char.upper())
#
# elif "A" <= char <= "Z":
#     print(char.lower())
#
# else:
#     print(f"The given character {char} is not an alphabet")

""" To check if the given string is a palindrome"""
#
# str_ = "malayal"
# rev_str = str_[::-1]
#
# if rev_str == str_:
#     print(f"The given string {str_} is a palindrome")
#
# else:
#     print(f"The given string {str_} is not a palindrome")

############################################################

"""To check if the given number is a palindrome """

# number = 123321
# str_number = str(number)
#
# if str_number[::-1] == str_number:
#     print(f"The given number {number} is a palindrome")
#
# else:
#     print(f"The given number is not a palindrome")

##############################################################

""" To check if the iterable has even number of elements"""

# list_ = [10, 20, 30]
#
# if len(list_) == 0:
#     print(f"The iterable is empty")
#
# elif len(list_) % 2 == 0:
#     print(f"The iterable {list_} has even number of elements")
#
# else:
#     print(f"The iterable {list_} has odd number of elements")

################################################################

"""To check if the first digit of the given number is even or odd"""
#
number = 7234
str_num = str(number)

if int(str_num[0]) % 2 == 0:
    print(f"The first digit {str_num[0]} is an even number")

else:
    print(f"The first digit {str_num[0]} is an odd number")

################################################################

