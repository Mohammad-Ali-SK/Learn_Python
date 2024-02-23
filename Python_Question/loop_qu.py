# Question-----------------------------------1.0)

# n = int(input("Enter number_"))
# for i in range(0,n+1):
#     print(i)

# Question ------------------------------2.0)

# n = int(input("Enter number_"))
# for i in range(n,0,-1):
#     print(i);

# Question --------------------------------3.0)
# num = int(input("Enter the number_"))
# for i in range(1,11,1):
#     print(f"{i} * {num} = {i*num}");

# Question ----------------------------------------4.0)

# num = int(input("Enter the num_"))
# ans = 0
# for i in range(0, num+1):
#     ans += i

# print(ans)

# Question -----------------------------------------5.0) **

# n = int(input("Enter the number -"))
# fact = 1
# for i in range(1,n+1):
#     fact = fact * i
# print(fact)

# Loops Advance Question's

# Q.6 Print all the factors of a number. -----------------------6.0) ***

# n = int(input("Enter the number_"))

# for i in range(1,n+1):
#     if n%i == 0:
#         print(i,end = " ")

# Question----------------------------------------------------------7.0) ***

# n = int(input("Enter your number_"))

# sum = 0

# for i in range(1,n+1):
#     if n%i == 0:
#         if i == n:
#             break
#         sum += i

# if sum == n:
#     print("this is a strong num")
# else:
#     print("not")

# Check a prime number or not ------------------------------------8.0)**

# n = int(input("Enter a num - "))
# count = 0
# for i in range(1,n+1):
#     if n%i == 0:
#         count = count + 1
# if count == 2:
#     print("This is prime num")
# else:
#     print("Composite number")

# n = int(input("Enter the num - "))
# count = 0
# for i in range(1 , n+1):
#     if n%i == 0:
#         count = count + 1
# if count == 2:
#     print("Prime")
# else:
#     print("Con")


# Q.9) Seprate each digit of a number and print it on the new line -------------------9.0)
# a = int(input("Enter number --"))
# while a > 0:
#     print(a%10)
#     a = a//10

# Q.10 --------------------------------------------------------------------10.0)
# a = int(input("Enter number --"))
# copy = a
# ch = 0
# while a > 0:
#     z = a%10
#     ch = ch * 10 + z
#     a = a//10
# print(ch)