# Content
# 1.) Function in python
# 2.) Strings
# 3.) List
# 4.) Tuple
# 5.) Dictionary
# 6.) Sets



# Function ----------------------------------- 1.0)
# inbuild function, Userdefined function

# def hello(a): -------Parameter
        #  print(a)
# hello(12)-------Argumenter

# def hello(a ,b,c = 0): -------- Default Parameter 
#     print(a + b) 
# hello(12,133, 67)      --------Default Argument

# def hello(a,b,c):
#     print(a + b + c)
# hello(c=56, b=34, a=1) ------Keywords Arg 

# def evenodd(a):
#     if a%2 == 0:
#         return("Even")
#     else:
#         return("Odd")
# for i in range(1,11):
#     print(evenodd(i))

# String -----------------------------------------------------------2.0)
# a = 'Mohammad ALI sk'
# print(a.upper())

# for i in range(0, len(a)):
#     print(a[i])

# Some of string Method in python-------
# format(), title(), isupper() , capitalize() , encode() , upper(), isnumeric() , index() , find() , islower() , isigit() , isalpha() , zfit()


# List in python -------------------------------------------------3.0)

# A list a vetsatile and mutable data structure that allows you to store a collection of items

# List indexing 
# List sliceing

# a = [34, 34, 89 , 'Mohammad ALI sk']
# a[1] = 67    --------------------------------List is mutable and every element can be change
# print(a)

# for i in range(0, len(a)):   ------range function in python
#     print(a[i])

# for i in a:
    # print(i)
    
# There are some of list method in python
# append("...")// adding at last
# insert(index, "....")//adding at particular index
# pop() "at the last" / (index) / return pop element
# removed("Item")

# Example of list method--------

# a = [13, 89, 90, 23, 76]

# a.append(777)
# a.pop()
# a.remove(13)
# a.insert(1,600)  ---------------Add anywhere in the list
# print(a)

# Tuple in python--------------------------------------------------------------- 4.0)

# This is read in semiler to tuple in python 

# tuple unpacking

# a = (1,2,3)
# print(a[2])
# a[0] = 78
# print(a)
# d,b,c = a     ---- This is tuple unpacking
# print(d)


# Set in python --------------------------------------------------------------5.0)
# Set is unique and unchangeable
# You can change list to set

# Dictionary Methods------------------------------------------6.0)
