# Under stand Decorators in python ____
# Decorators like a toll _boot.

# Learn About Decorators in python_____
# Problem 1: Timing Function Execution----------------------------

# import time
# def timer(func):
#     def wrapper(*args,**kwargs):
#         start = time.time()
#         result = func(*args,**kwargs)
#         end = time.time()
#         print(f'{func.__name__} ran in {start - end}')
#         return result
#     return wrapper

# @timer
# def example_fun(n):
#     time.sleep(n)
    
# example_fun(2)
# import time

# def my_func(func):
#     def wrapper(*args):
#         print('Good MOrning')
#         func(*args)
#         print('Good afternooon')
#     return wrapper
# @my_func
# def user(a,b):
#     print(a+b)
#     print('Mohammad ALi sk')
#     time.sleep(2)
# user(1,2)


# def avarage(*numberrs):
#     print(numberrs)
#     sum  = 0
#     for i in numberrs:
#         sum = sum + i
#     print("Avarage  is  : ", sum / len(numberrs))
    
# avarage(6,9,9,98,87)


# *numbers-----------------------------Store like a tuple.
# **name ------------------------------store like a dictionary.