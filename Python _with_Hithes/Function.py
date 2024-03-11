# Solve 10 problems on functions in python
# def sum(a,b):
#     return a + b
# print(sum(67,3))


# 03_Solution
# import math
# def circle_stats(radius):
    
# print(int(circle_stats(8)))


#0_7 solution
# Functiion with *args   -----------Use of Args****

# def sum_all(*args):
#     print(*args)
#     for i in args:
#         print(i * 2,end = ' ')
#     return sum(args)

# print(sum_all(1,23,45,67,67))

# 0_8 Function with **kwargs-------------------------Sulutiion--0.8)

# def print_kwargs(**kwargs):
#     for key, value in kwargs.items():
#         print(f'{key} : {value}')

# print_kwargs(name = 'Mohammad ALi sk', power = 'Lighrt')
# print_kwargs(name = 'Iron man' , power = 'All-rounder')
 
# 0_9 Solution -------------Generate Function with yelled       -----Understand Yield

# def even_gen(limit):
#     for i in range(2, limit+1,2):
#         yield i

# for num in even_gen(10):
#     print(num)

# 10_Solution-----------------------------------Recursive Function
