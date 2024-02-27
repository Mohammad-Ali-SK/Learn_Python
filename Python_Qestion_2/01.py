# Advance Logic making
# Question in string
# Question in list
# Question in DIctionary


# Question on String------------------------------------------1.0)
# Reverse in the string ----------1.1)

# a = "Mohammad ALi sk"
# b = ''
# for i in range(len(a)-1, -1, -1):
#     b = b + a[i]
# print(b)

# Method  ----2
# print(a[:: -1])


# Question---------------------------------------------1.2)
# Arrange string characters such that lowweercase letters should come first in another string
# a = "you BroThEr HoW ArE You"

# b = ''
# for i in n:
#     if i.islower():
#         b = b + i
# for i in n:
#     if i.isupper():
#         b = b + i
# print(b)


#Question -------------------------------------------1.3)
# Count all letters , digits , and special symbols from a given string
# a = 'P@#yn26at^&i5ve'
# char = 0
# dig = 0
# symb = 0
# for i in a:
#     if i.isdigit():             #Find Number
#         dig = dig + 1
#     elif i.isalpha():          #find character                    
#         char = char + 1
#     else:
#         symb = symb + 1
# print(f"Your counting letters is {char} and digits is {dig} and special num is {symb}")

# Question ---------------------------------------------1.4)
# Count Vowels from given string

# a = "I am ALi e E oj and U h u"
# c = 0
# for i in a:
#     if i in  'Aeiou':
#         c = c + 1
# print(c)


#  Use function in python--------

# def checkVol(a):
#     vol = 0
#     cons = 0
#     for i in a:
#         if i in "AaEeIiOoUu":
#             vol = vol + 1
#         elif i in " ":
#             continue
#         else:
#             cons = cons + 1
#     print(vol, cons)

# checkVol("a e i o u x s d")

# Question -----------------------------------------------------------1.5)
# Check string is Pallindrome or not
# a = "naman"
# b = ''
# for i in range(len(a) -1, -1,-1):
#     b = b + a[i]

# if a == b:
#     print("Pallindrone")
# else:
#     print("GO away")

# List Question in python ---------------------------------------------------2

# Question -----------------------------------------------------------------2.1)
# Accept list element and reprint it
