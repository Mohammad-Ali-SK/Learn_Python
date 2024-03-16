
# # debugg
# def debug(func):
#     def wrapper(*args,**kwargs):
#         return func(*args, **kwargs)
#     return wrapper




# @debug
# def greet(name,greeting='Hello'):
#     print(f"{greeting}, {name}")
    
# greet('Ali', greeting='Yt')
# import time

# def cash(func):
#     cash_val = {}
#     def wrapper(*args):
#         if args in cash_val:
#             return cash_val[args]
#         result = func(*args)
#         cash_val[args] = result
#         return result
#     return wrapper

# @cash
# def long_running_function(a,b):
#     time.sleep(4)
#     return a+b
# print(long_running_function(2,3))
# print(long_running_function(9,3))
# print(long_running_function(4,3))

# def cash(func):
#     cash_val = {}
#     def wrapper(*args):
#         if args in cash_val:
#             return cash_val[args]
#         result = func(*args)
#         cash_val[args] = result
#         return result
#     return  wrapper

# @cash
# def example_in(a,b):
#     time.sleep(4)
#     return a + b
# print(example_in(1,2))
# print(example_in(3,5))
# print(example_in(5,9))
