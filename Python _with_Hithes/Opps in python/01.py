# polymorphisom
# class Car:
#     total_car = 0
#     def __init__(self,name,model):
#         self.name = name
#         self.model = model
#         Car.total_car += 1
#     def details(self):
#         print(f'{self.name} {self.model}')
    
# safari = Car('Tata', 'Safari')
# car_2 = Car('Lam','S-20')
# print(Car.total_car)

# Property Decorators-----
# Problem:-Use a property decorator in the Car class to make the model attribute read-only.

# Decorators in python----------------------------------------------
# Problem _1 : Timing Function Execution

# def debug(func):
#     def wrapper(*args,**kwargs):
#         return func(*args,**kwargs)
    
#     return wrapper

# debug()



# def greet(name,greeting = 'Hello'):
#     print(f'{greeting} , {name}')
    
# greet('ali', greeting='yt')
import time

# def timer(func):
#     def wrapper(*args,**kwargs):
#         start = time.time()
#         result = func(*args,*kwargs)
#         end = time.time()
#         print(f"{func.__name__} ran in {end - start}")
#         return result
#     return wrapper

# @timer
# def example_fun(n):
#     time.sleep(n)

# example_fun(2)
#
# Debugging Function Calls ------------------------------------



