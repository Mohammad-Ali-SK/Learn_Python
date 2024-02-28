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
# l = []
# count = int(input("Enter how many number are you wnat - -"))
# for i in range(count):
#     z = int(input("Enter the number -- "))
#     l.append(z)
# print(l)

# Question list item in revers order ------------------------------2.2)

# l = []
# count = int(input("Enter the counter ----"))

# for i in range(count):
#     z = int(input("Enter the number ---"))
#     l.append(z)
# print(l)

# v = []
# for i in range(len(l) -1, -1, -1):
#     v.append(l[i])

# print(v)

# Question ----------------------------------------------2.3)
# Print positive and negative elements of an list in seprate list
# a = [1,-3, 2, 8 , -8, 9, -5]
# pos = []
# neg = []
# for i in range(1, len(a)):
#     if a[i] > 0:
#         pos.append(a[i])
#     elif a[i] < 0:
#         neg.append(a[i])
#     else:
#         print("Nothig here")
# print(pos)
# print(neg)

# Question ----------------------------------- 2.4)
# Find the greatest elemnet and print its index too.
# list = [2, 96, 89, 19 , 165]

# m = 0
# index = 0

# for i in range(len(list)):
#     if list[i] > m:
#         m = list[i]
#         index = i

# print(m, index)

# QUestion ------------------------------------------------------2.5)
# Find the second gretest number
# a = [12, 33, 89, 67, 900, 677, 45,9778, 99, 786]
# max = 0
# max2 = 0
# index = 0
# index2  = 0

# for i in range(len(a)):
#     if a[i] > max:
#         max2 = max
#         max = a[i]
#         index2 = index
#         index = i
#     elif a[i] > max2:
#         max2 = a[i]
#         index2 = i
# print(max , index)
# print(max2, index2)

# Question -----------------------------------------------2.6)
# Check if list is sorted or not
# a = [1,2,3,4,5,6,7]
# for i in range(len(a)-1):
#     if a[i] < a[i + 1]:
#         continue
#     else:
#         print("Your list is not sorted")
#         break
# else:
#     print("Your list is shorted")

# Question --------------------------------------------2.7)

# Pallindromic list - write a program to check if element of an list are samee or not it read from front or backExamle :

# list = [2,3,15,15,3,2]
# list_2 = []
# for i in range(len(list) - 1, -1, -1):
#     list_2.append(list[i])
# if list == list_2:
#     print("Pallindromic")
# else:
#     print("Not a pallindromic")

# Question -----------------------------------------------2.8)
# How many seprate elements are there in the list excluding repetation.



# Dictionary Questiion in python ---------------------------------------------------------

# Question ----------------------------------------------- 1.0)
# Write a python script to merge two python dictionaries.

# a = {1:10,2:20,3:30,4:40}
# b = {7:70,8:80,9:90}
# c = a
# c.update(b)
# print(c)


# Question ---------------------------------------------- 2.0)
# Write a python program to sum all the values in a dictionary.
 
# dis = {1:10,2:30,5:90}
# sum = 0
# for i in dis.values():
#     sum = sum + i
    
# print(sum)


# Question ------------------------------------------------3.0)
# count the frequency of each elements in a list
# a = [1,2,3,3,5,2,13,5,1,2,4,1,2,4,13,2,13,22,4,2,3,1,13,4,2,4,2]
# dict = {}
# for i in a:
#     if i in dict.keys():
#         dict[i] = dict[i] + 1
#     else:
#         dict[i] = 1
# print(dict)


# Question ------------------------------------------------------4.0)
# Write a python program to combibe two dictionary by addding values for common keys
a = {1:10,2:20,3:30,4:40}
b = {7:70,2:80,9:90}

for i in b.keys():
    if i in a.keys():
        a[i] = a[i] + b[i]
    else:
        a[i] = b[i]
print(a)