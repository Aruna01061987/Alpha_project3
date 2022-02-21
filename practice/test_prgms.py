""" remove all the duplicate elements """

# l = ["a", "b", "c", "d", "b", "c"]

# print(list(set(l)))

# res = []
# for item in l:
#     if item not in res:
#         res.append(item)
#
# print(res)
#
# res1 = []
#
# for item in l:
#     if l.count(item) == 1:
#         res1.append(item)
#
#
# print(res)

""" print numeric value in the list """

# items = ["python", 1.2, 9, 1 + 2j, [1, 2, 3], True]
#
# for item in items:
#     if isinstance(item, (int, float, complex)):
#         print(item)

""" sum of all even numbers in the string """
# string = "alpha3python127 selenium12,47956"

# sum1 = 0
#
# s = list(string)

# for char in s:
#     if '0' <= char <= '9' and int(char) % 2 == 0:
#         sum1 += int(char)
#
# print(sum1)

# for char in s:
#     if char.isdigit() and int(char) % 2 == 0:
#         sum1 += int(char)
#
# print(sum1)

""" create a set of languages starting with "p" """

# languages = ["python", "java", "Perl", "PHP", "Python"]
# s = set()
#
# for language in languages:
#     if language[0] in 'Pp':
#       s.add(language)
#
# print(s)

""" list with only even length string """

# languages = ["python", "java", "Perl", "PHP", "Python"]
#
# evens = []
# even = [language for language in languages if len(language) % 2 == 0]
#
# for language in languages:
#     if len(language) % 2 == 0:
#         evens.append(language)
#
# print(even)
# print(evens)

""" reverse if odd length else keep it as it is """

# languages = ["python", "java", "Perl", "PHP", "Python", "c++", "node JS"]
#
# odd_len = []
#
# for language in languages:
#     if len(language) % 2 != 0:
#         odd_len.append(language)
#
# print(odd_len)
#
# odd_lens = [language for language in languages if len(language) % 2 != 0]
#
# print(odd_lens)

# l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# entire_sum = 0
#
# for item in l:
#     internal_sum = 0
#     for i in item:
#         internal_sum += i
#         entire_sum += i
#     print(internal_sum)
# print(entire_sum)

""" list of prime numbers from 1 to 100"""
# prime = []
# for num in range(1, 101):
#     if num > 1:
#         for i in range(2,num):
#             if num % i == 0:
#                 break
#         else:
#             prime.append(num)
#
# print(prime)

""" reverse the list """

# list_ = ["hi", "hello", "python"]
#
# print(list_)
# k = list_.sort(reverse=True)
# print(k)

# n = ["a", "g", "b"]
# print(n.sort())

"""WAP to reverse the items in the list"""

# l = ["hi", "hello", "python"]
# res = []
# print(l[::-1])
#
# for item in l[::-1]:
#     res.append(item[::-1])
#
# print(res)

""" rotating the list based on k value """

# languages = ["python", "java", "Perl", "PHP", "C"]
# k = 2

# for i in range(k+1):
#     item = languages.pop()
#     languages.insert(0, item)
#
# print(languages)

languages = ["python", "java", "Perl", "PHP", "C"]


# for item in range(len(languages)+1):
# k = 2
# for i in range(k):
#     temp = languages.pop()
#     languages.insert(0, temp)
#
# print(languages)

############################string assessments############################

""" no of digits and alphabets"""
# string = "hello$&#123hai8AVB"
# digit_count = 0
# alpha_count = 0
#
# for char in string:
#     if 'a' <= char.lower() <= 'z':
#         alpha_count += 1
#     elif '0' <= char <= '9':
#         digit_count += 1
#     else:
#         pass
#
# print(f"alphabets count is {alpha_count}, digits count is {digit_count}"


""" create a string by swapping the cases"""

# s = "HeLlo WOrlD"
# res = ""

# for char in s:
#     res += char.swapcase()
#
# print(res)

# for char in s:
#     if 'a' <= char <= 'z':
#         res += chr(ord(char) - 32)
#     elif 'A' <= char <= 'Z':
#         res += chr(ord(char) + 32)
#     else:
#         res += char
#
# print(res)


""" create a string with consonants """

# s = "hello world90#%"
# res = ""
#
# for char in s:
#     if char.lower() in 'aeiou':
#         pass
#     else:
#         res += char
#
# print(res)

""" search for a character and return its first occurrence index """

# s = "hello world"
#
# char = 'l'
#
# # for i in s:
# #     if char == i:
# #         print(s.index(i))
# #         break
#
# for index, item in enumerate(s):
#     if char == item:
#         print(f"character is at index:{index}")
#         break

""" print char and ascii value if it is a vowel"""
# s = "hello WOrld"
#
# for char in s:
#     if char.lower() in 'aeiou':
#         print((char, ord(char)))


""" print word and its length"""
# s = "hello world hai how are you?"
#
# words = s.split()
#
# for word in words:
#     print((word, len(word)))

""" print words starting with vowels """
# sentence = " hai everyone, welcome to the python class economics"
#
# words = sentence.split()
#
# for word in words:
#     if word[0].lower() in 'aeiuo':
#         print(word)

""" count the characters without any inbuilt functions """
# s = "hello world"
#
# count = 0
#
# for char in s:
#     count += 1
#
# print(count)

""" reversing a string """
# string = "hello"
#
# print(string[::-1])

# for char in reversed(string):
#     print(char, end="")
# str_ = ""
# for char in range(len(string)-1,-1, -1):
#     str_ += string[char]
#
# print(str_)

# res = ""
# for char in string:
#     res = char + res
#
# print(res)

##############################   dict comprehensions ########################################################

""" WAP to create a dictionary with item and its index pair"""

# normal method
# string = "hello"

# normal method

# d = {}
# for index, item in enumerate(string):
#     d[item] = index
#
# print(d)
#
# # using dict comprehensions
# d_ = {item: index for index, item in enumerate(string)}
#
# print(d_)

""" WAP to create a dictionary with word and its length pair"""
# sentence = "hello world welcome to python"

# normal method
# d = {}

# words = sentence.split()

# for word in words:
#     d[word] = len(word)
#
# print(d)

# d_ = {word: len(word) for word in words}
# print(d_)

""" create a dictionary of character and its count"""
# s = "hello world"
#
# d = {}
#
# for char in s:
#     d[char] = s.count(char)
#
# print(d)
#
# d_ = {char: s.count(char) for char in s}
# print(d_)

# """ create a dictionary of word and its count"""
# sentence = "python is a language, python programming is easy"
#
# words = sentence.split()
#
# d = {}
#
# for word in words:
#     d[word] = words.count(word)
#
# print(d)
#
# d_ = {word: words.count(word) for word in words}
#
# print(d_)


""" dictionary with word and its count pair only if the word is of even length"""

# sentence = "python is a language, python programming is easy"
#
# words = sentence.split()
#
# d = {}
#
# for word in words:
#     if len(word) % 2 == 0:
#         d[word] = words.count(word)
#
# print(d)
#
# d_ = {word: words.count(word) for word in words if len(word) % 2 == 0}
# print(d_)

""" dictionary with index and word pair if the word is of odd length reverse it,
else keep it as is"""

# sentence = "python is a language, python programming is easy"
# words = sentence.split()
# d = {}
#
# for index, word in enumerate(words):
#     if len(word) % 2 == 0:
#         d[index] = word
#     else:
#         d[index] = word[::-1]
#
# print(d)
#
# d_ = {index: word if len(word) % 2 == 0 else word[::-1] for index, word in enumerate(words)}
#
# print(d_)

""" word and length pair only if the word is starting with vowel """

# sentence = "python is a language, python programming is easy"
# words = sentence.split()
# d ={}
#
# for word in words:
#     if word[0].lower() in 'aeiou':
#         d[word] = len(word)
#
# print(d)
#
# d_ = {word: len(word) for word in words if word[0].lower() in 'aeiou'}
# print(d_)

""" index and word pair if word is of type string reverse it """
# list_ = ["python", 17, 9, "java", 19.9, 4+0j, "ruby", "c++"]
#
# d = {}
#
# for index,item in enumerate(list_):
#     if isinstance(item, str):
#         d[index] = item[::-1]
#     else:
#         d[index] = item
#
# print(d)
#
# d_ = {index: item[::-1] if isinstance(item, str) else item for index, item in enumerate(list_)}
#
# print(d_)

""" index and word pair if word is of type string keep it as it else reverse it """
# list_ = ["python", 17, 9, "java", 19.9, 4+0j, "ruby", "c++"]

# d = {}
#
# for index,item in enumerate(list_):
#     if isinstance(item, str):
#         d[index] = item[::-1]
#     else:
#         d[index] = item
#
# print(d)
#
# d_ = {index: item[::-1] if isinstance(item, str) else item for index, item in enumerate(list_)}
#
# print(d_)

""" index and word pair if word is of type string keep it as it else reverse it """

# list_ = ["python", 17, 9, "java", 19.9, 4+0j, "ruby", "c++"]
# d = {}
#
# for index, item in enumerate(list_):
#     if isinstance(item, str):
#         d[index] = item
#     else:
#         d[index] = str(item)[::-1]
#
# print(d)
#
# d_ = {index: item if isinstance(item, str) else str(item)[::-1] for index, item in enumerate(list_)}
# print(d_)

""" flip keys and values in a dictionary """
# dict_ = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}

# for key,value in enumerate(dict_):
#     dict_[value] = key
#
# print(dict_)

# d = {value: key for key, value in enumerate(dict_)}
# print(d)

# d = {value: key for key, value in dict_.items()}
# print(d)

# d_ = {}
#
# for key,value in dict_.items():
#     d_[value] = key
# print(d_)
#
# res = {dict_[key]: key for key in dict_}
# print(res)

""" char and ascii value pair """
# string = "python"
#
# d = {char: ord(char) for char in string}
# print(d)

################################### list comprehensions ###############################################

""" WAP to create a list of squares for the elements in the below list"""
# l = [1, 2, 3, 4, 5]
# nl = []
#
# for num in l:
#     nl.append(num ** 2)
# print(nl)
#
# new_list = [num ** 2 for num in l]
# print(new_list)
#
# new_list1 = [pow(num, 2) for num in l]
# print(new_list1)

""" create list of tuples of index and its corresponding item in the list """
# l = ["python", 10, 3.2, "selenium", "Java"]
#
# nl = []
#
# for index, item in enumerate(l):
#     nl.append((index, item))
#
# print(nl)
#
# new_list = [(index, item) for index, item in enumerate(l)]
# print(new_list)

# new_list1 = [item for item in enumerate(l)]
# print(new_list1)

""" list of even numbers """
# l = list(range(10))
#
# print(l)
#
# evens = []
#
# for i in l:
#     if i % 2 == 0:
#         evens.append(i)
#
# print(evens)
#
# comp_list =[i for i in l if i % 2 == 0]
# print(comp_list)

""" list of even and odd in the given range"""

# list_ = list(range(20))
# evens = []
# odds = []

# for i in list_:
#     if i % 2 == 0:
#         evens.append(i)
#     else:
#         odds.append(i)
#
# print(evens, odds)

# evens = [i for i in list_ if i % 2 == 0]
# odds = [i for i in list_ if i % 2 != 0]
#
# print(evens, odds)

""" if even length store as it is else reverse and store it """
# l = ["python", "Node JS", "selenium", "Java"]
#
# new_list = [item if len(item) % 2 == 0 else item[::-1] for item in l]
# print(new_list)

""" reverse if it is a string else keep it as it is """
# list_ = ["Java", "Python", 10, True, 1.4, "c++", "ruby"]
#
# new_list = [item[::-1] if isinstance(item, str) else item for item in list_]
# print(new_list)

""" list of words starting with vowel """
# files = ["Amazon", "flipkart", "walmart", "gmail", "yahoo"]
#
# vowel_list = [word for word in files if word[0].lower() in 'aeiou']
# print(vowel_list)

################################### set comprehension ######################################

""" set comprehension to create a set of squares from 1 to 10"""

# l= list(range(11))
#
# s = {pow(i,2) for i in l}
# print(s)

""" set of tuples with index and item """
# list_ = ["Java", "Python", 10, True, 1.4, "c++", "ruby"]
#
# s = {(index, item) for index, item in enumerate(list_)}
# print(s)
#
# set_ = {item for item in enumerate(list_)}
# print(set_)

""" set of tuples with item and its length pair """
# files = ("Amazon", "flipkart", "walmart", "gmail", "yahoo")
#
# s = {(item, len(item)) for index, item in enumerate(files)}
# print(s)

###################################### if- condition ####################################

""" WAP to check if the given input number is even"""

# num = 18
#
# if num % 2 == 0:
#     print('even')
# else:
#     print('odd')

""" WAP to check if the given character is in lowercase """

# char = 'l'
#
# if 'a' <= char <= 'z':
#     print(f"character {char} is in lowercase")

# if char.islower():
#     print("character is in lower case")

""" WAP to check if the element in present in collection """


# list_ = ["python", "java", "linux", "ruby", "nodejs"]
# element = "java"
#
# if element in list_:
#     print("the element is present")

""" WAP to check if the character is lowercase or uppercase"""

# char = "o"

# if 'a' <= char <= 'z':
#     print('char is in lowercase')
# else:
#     if 'A' <= char <= 'Z':
#         print('char is in uppercase')
#     else:
#         print('char is not an alphabet')

# if 'a' <= char <= 'z':
#     print('char is in lowercase')
# elif 'A' <= char <= 'Z':
#     print('char is in uppercase')
# else:
#     print('char is not an alphabet')

# if char.islower():
#     print("lower")
# elif char.isupper():
#     print("upper")
# else:
#     print('char is not an alphabet')

""" WAP to check if the given iterable is empty or not """

# iterable = ""
#
# if iterable:
#     print("not empty")
# else:
#     print('empty')

""" WAP to check if the given value is default or non default value"""

# value = [1]
#
# if value:
#     print('non default')
# else:
#     print('default')

""" WAP to convert lowercase to uppercase and vice-versa """

# char = "B"
#
# if 'a' <= char <= 'z':
#     print(chr(ord(char)-32))
# elif 'A' <= char <= 'Z':
#     print(chr(ord(char)+32))
# else:
#     print("not a character")
#
# if char.islower():
#     print(char.upper())
# elif char.isupper():
#     print(char.lower())
# else:
#     print('not a character')

# number = 1221
# str_num = str(number)
#
# if number == int(str_num[::-1]):
#     print('number is a palindrome')
# else:
#     print('number is not a palindrome')

# char = "a"
# d = {}
# if char.lower() in "aeiou":
#     # d[char] = ord(char)
#     #  d.update({char: ord(char)})
#     # d.setdefault(char, ord(char))
#     print({char: ord(char)})
#
# print(d)

# d = {}
# d.setdefault("python")
# print(d)
# d.setdefault("Java", 4)
# print(d)

######################################### functions ########################################

""" check if the number is prime or not"""


# def prime_(num):
#
#     for i in range(2, num):
#         if num % i == 0:
#             return "number is not prime"
#     return "number is prime"
#
#
# print(prime_(8))

""" to return last digit of an integer """

# def last_digit(num):
#     # return num % 10
#     return str(num)[-1]
#
#
# print(last_digit(1234))

""" return last n elements from the sequence """


# def tail(sequence, n):
#     return sequence[-n:]
#
#
# print(tail("hello", 3))

""" square or not"""

# def is_square(num):
#     for i in range(num):
#         if i*i == num:
#             return f"The num:{num} is a perfect square"
#     return f"the number is not a perfect square"
#
# print(is_square(24))
#
#
# def square(num):
#     sq = int(num ** 0.5)
#     if sq ** 2 == num:
#         return f"the number is perfect square number"
#     return f"the  number is not perfect square number"
#
#
# print(square(49))

""" func("TRACXN", 0)   # should print RCN
    func("TRACXN", 1)   # should print TAX"""


# def func(str_, num):
#     if num == 0:
#         return str_[1::2]
#     elif num == 1:
#         return str_[::2]
#     else:
#         return "n is invalid number"
#
#
# print(func("TRACXN", 4))


""" check if the number is fibonacci number or not"""


# def is_fibo(num):
#     a = 0
#     b = 1
#     while a <= num:
#         if a == num:
#             return "the number is a fibonacci number"
#         c = a + b
#         a = b
#         b = c
#     return "number is not a fibonacci number"
#
#
# print(is_fibo(3))


""" length of iterables """

# def iterable_length(*args):
#     for item in args:
#         if isinstance(item, (str, list, tuple, set, dict)):
#             print(item, len(item))
#
#
# iterable_length("python", [1,2,3,4], {5,6,7,8}, (23, 45, 56,))

""" to print all the perfect square numbers in a given range """

# names = ["apple", "google", "gmail", "yahoo", "gmail", "apple", "gmail", "google"]
#
# # normal dictionary
# d = {}
#
# for index, item in enumerate(names):
#     if item not in d:
#         d[item] = [index]
#     else:
#         d[item] += [index]
#
# print(d)


# print("today is beautiful day".rfind("day"))
#
# print("today is beautiful day".find("day"))
#
# from collections import defaultdict
# s = "hello world"
# dd = defaultdict(int)
# print(dd)
#
# for char in s:
#     dd[char] = dd[char] + 1
#
# print(dd)
#
# from collections import defaultdict
# s = "hello world"
# dd = defaultdict(int)
# print(dd)
#
# for char in s:
#     # dd[char] = s.count(char)
#     dd[char] += 1
# print(dd)

# s = "hello world"
# d = {}
#
# for char in s:
#     if char not in d:
#         d[char] = 1
#     else:
#         d[char] += 1
#
# print(d)

# r = "replace practice"
# d1 = {}

# for char in r:
#     if char not in d1:
#         d1[char] = 1
#     else:
#         d1[char] += 1
#
# print(d1)
#
# from collections import defaultdict
#
# dd= defaultdict(int)
#
# for char in r:
#     dd[char] += 1
#
# print(dd)


""" word and its length pair """
# sentence = "python is a language, python programming is easy"
# list_ = sentence.split()
# d = {}
#
# for word in list_:
#     d[word] = len(word)
#
# print(d)

# l = ["hello", "ball", "zebra", "yak", "apple"]
#
# print(sorted(l, key = lambda item: item[0]))
#
# prices = {'ACME': 45.23, 'AAPL': 612.76, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75}
#
# res = sorted(prices.items(), key = lambda item:  item[1] > float(40))
# print(res)


# def is_anagram(str1, str2):
#     if len(str1) == len(str2):
#         for char in str1:
#             if char in str2:
#                 return True
#             else:
#                 return False
#
#
# print(is_anagram('silent', 'listen'))

#
# def count_(n):
#     if n <= 10:
#         print(n)
#         return count_(n+1)
#
#
# print(count_(1))


#
# s = 'AABBCCCDAACD'
#
# str_ = []
#
# for i in range(len(s)):
#     str_ = []
#     k = len(s)//3
#     for j in range(k):
#         if j % 2 == 0:
#             str_.append(s.count(s[j]))
#         else:
#             str_.append(s[j])
#
#
# print(str_)
#
# sentence = 'see and saw went to see a sea'
#
# words = sentence.split()
# set_ = set(words)
#
# res = sorted(set_, key=lambda word: len(word))
#
# print(res[-1])


# sentence = "12 plus 18 equals to 30"
# words = sentence.split()
# print(words)
#
# d = {word: word[::-1] if word.isnumeric() else word for word in words}
#
# print(d)

# s = r"hai \tha\nk you"
# print(s)

# s = {1, 2, 3}

# str_ = "durga"

# ns = ""
#
# for i in str_:
#     ns = i + ns
#
# print(ns)

# rs = ""
#
# i = len(str_)-1
#
# while i >= 0:
#     rs = rs + str_[i]
#     i = i-1
#
# print(rs)

# for char in range(len(str_)):
#     rs = str_[char] + rs
#
# print(rs)

# sentence = "learning python is very easy"
#
# words = sentence.split()
#
# l = []
#
# for word in reversed(words):
#     l.append(word)
#
# print(" ".join(l))

# words = sentence.split()
# i = len(words)-1
# l = []
#
# while i >= 0:
#     l.append(words[i])
#     i = i-1
#
# print(" ".join(l))

# words = sentence.split()
#
# l = []
#
# for i in range(len(words)-1, 0, -1):
#     l.append(words[i])
#
# print(" ".join(l))

# words = sentence.split()
# print(" ".join(words[::-1]))

"""WAP to reverse the internal content of the words"""

# sentence1 = "Durga software solutions"
# words = sentence1.split(" ")

# using slicing[::-1]
# ns = []
#
# for word in words:
#     ns.append(word[::-1])
#
# print(" ".join(ns))

# Using reversed
#
# nl = list(sentence1)
# nl1 = []
#
# for char in reversed(nl):
#     nl1.append(char)
#
# print(" ".join(nl1))

"""WAP to reverse internal content of every second word present in the string"""

# using enumerate function

# string_ = "one two three four five"
#
# words = string_.split()

# new_list = (value[::-1] if index % 2 != 0 else value for index, value in enumerate(words))
# print(str(" ".join(new_list)))

# using while loop

# string_ = "one two three four five"
# new = []
# words = string_.split()
# i = 0
#
# while i < len(words):
#     if i % 2 == 0:
#         new.append(words[i])
#     else:
#         new.append(words[i][::-1])
#     i = i + 1
#
# print(" ".join(new))


"""WAP to print characters at even and odd indexes"""

# s = "durgasoft"
#
# odd = []
# even = []
#
# i = 0
# while i < len(s):
#     even.append(s[i])
#     i = i + 2
#
# i = 1
# while i < len(s):
#     odd.append(s[i])
#     i = i + 2
#
# print(odd)
# print(even)

#  using enumerate

# s = "durgasoft"
# even = []
# odd = []
# for index,char in enumerate(s):
#     if index % 2 == 0:
#         even.append(char)
#     else:
#         odd.append(char)
#
# print(f"even indexed characters:{even}")
# print(f"odd indexed characters:{odd}")

# using slicing

# s = "Durgasoft"
#
#
# even = list(s[::2])
# odd = list(s[1::2])
#
# print(even)
# print(odd)

#  Using for loop

# s = "Durgasoft"
# even = []
# odd = []
#
# for i in range(0,len(s)):
#     if i % 2 == 0:
#         even.append(s[i])
#     else:
#         odd.append(s[i])
#
# print(f"even: {even}")
# print(f"odd: {odd}")


"""WAP to sort the characters of the string, first alphabets symbols followed by digits """

# str_ = "B4A1D3"
# expected output: "ABD134"
# num = []
# alph = []
#
# for i in str_:
#     if i.isalpha():
#         alph.append(i)
#     else:
#         num.append(i)
#
#
# print("".join(sorted(alph) + sorted(num)))

# i = 0
# while i < len(str_):
#     if "A" <= str_[i].upper() <= "Z":
#         alph.append(str_[i])
#     elif "0" <= str_[i] <= "9":
#         num.append(str_[i])
#     else:
#         pass
#     i = i+1
#
# print("".join(sorted(alph) + sorted(num)))

"""WAP to get the output in the following format"""
# input = A4B3C2
# output = AAAABBBCC

# str_ = "a4b3c2"
#
# str1 = ""
#
# i = 0
#
# while i < len(str_):
#     if str_[i].isalpha():
#         ch = str_[i]
#     else:
#         str1 = str1 + ch * int(str_[i])
#
#     i = i+1
#
# print(str1)

"""WAP for the following requirement"""

# input: a3z2b4
# output: aaabbbbzz

# str_ = "a3z2b4"
#
# str1 = ""
#
# i = 0
#
# while i < len(str_):
#     if str_[i].isalpha():
#         ch = str_[i]
#     else:
#         str1 = str1 + ch * int(str_[i])
#
#     i = i+1
#
# print("".join(sorted(str1)))

"""WAP for the following requirement"""
# input: aaaabbbccz
# output: 4a3b2c1z

str_ = "aaaabbbccz"

new = ""
previous = str_[0]
count = 1
# i = 1
# while i < len(str_):
#     if str_[i] == previous:
#         count += 1
#         print(count)
#     else:
#         new = new + str(count) + previous
#         previous = str_[i]
#         count = 1
#     if i == len(str_)-1:
#         new = new + str(count) + previous
#     i = i+1
# print(new)


for i in range(1,len(str_)):

    if str_[i] == previous:
        count += 1
    else:
        new = new + str(count) + previous
        previous = str_[i]
        count = 1
    if i == len(str_)-1:
        new = new + str(count) + previous

print(new)






























