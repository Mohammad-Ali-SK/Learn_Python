# Question-----------------------------------1.0)
# a = int(input('Enter the num__'))
# for i in range(1,a+1):
#     print(i)

# Question ------------------------------2.0)

# n = int(input("Enter number_"))
# for i in range(n,0,-1):
#     print(i)
# Question --------------------------------3.0)
# n = int(input('Enter the number__'))
# for i in range(1,n+1):
#     print(f'{i} * {n} = {i*n}')

# Question ----------------------------------------4.0)
# n = int(input('Enter the num_'))
# sum = 0
# for i in range(1,n+1):
#     sum = sum + i
# print(sum)



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
#         print(i, end=" ")
    


# Question----------------------------------------------------------7.0) ***

# n = int(input('Entr the numbeer__'))
# sum = 0

# for i in range(1,n):
#     if n%i == 0:
#         sum += i
# print(sum)

# Check a prime number or not ------------------------------------8.0)**

# n = int(input('Enter the num__- )


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

# Home Work Question--------------------------
# n = int(input("Enter the number-"))

# n = int(input('Enter the number__'))
# sum = 0
# for i in range(1,n):
#     if n%i == 0:
#         sum = sum + i
# print(sum)

# a = int(input('Enter number__'))
# count = 0

# for i in range(1,a+1):
#     if a%i == 0:
#         count = count + 1
# if count == 2:
#     print('Prime')
# else:
#     print('Cons')


# n = int(input('Enter the number__-'))

# a = int(input("Please tell your number  -")) 
# a = 132
# copy = a
# rev= 0
# while a > 0:
#     z = a%10
#     rev= rev*10 + z
#     a = a//10
# print(rev)




n = int(input('Enter the number__'))

count = 0

for i in range(1,n+1):
    if n%i == 0:
        count = count + 1
print(count)