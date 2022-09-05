# ##-------------Fabinocci number-------------###
# a=0
# b=1
# for i in range(1,51):
#     print(i, ' - ', a)
#     c = a
#     a = b
#     b = c + b
# print('END')

###--------------Prime number check----------##
# p = int(input("Enter number to check if prime or not: "))
# count = 0
# if p==1 or p==2:
#     print(p, " is a prime number")
# else:
#     for i in range(2,int(p/2)+ 1):
#         if p%i == 0:
#             count +=1
#             #print(i)
#             break
#     if count>0:
#         print(p, ' is not a prime number')
#     else:
#         print(p,' is a prime number')



# ###-------print prime numbers upto given number----###
# n = int(input('Enter a number: '))
# if n<1:
#     print(n,' is not a valid number')
# elif n==1:
#     print(1)
# elif n==2:
#     print(1)
#     print(2)
# else:
#     print(1)
#     print(2)
#     j=3
#     while j<=n:
#         count = 0
#         for i in range(2,int(j/2)+1):
#             if j%i == 0:
#                 count +=1
#                 break
#         if count == 0:
#             print(j, ' ', end="")
#         j +=1

# ##-------------------------------------------------------------------##


# ##--------------------patterns----------------------------------------##
# n = int(input('How many rows do u need: '))
# for i in range(n):
#     for j in range(n):
#         print('# ', end="")
#     print()
# ###---------------------------------------------------------------------##

# ##--------------------patterns----------------------------------------##
# n = int(input('How many rows do u need: '))
# for i in range(n):
#     for j in range(i+1):
#         print('# ', end="")
#     print()
# ###---------------------------------------------------------------------##

# ##--------------------patterns----------------------------------------##
# n = int(input('How many rows do u need: '))
# for i in range(n):
#     for j in range(n-i):
#         print('# ', end="")
#     print()
# ###---------------------------------------------------------------------##

# ##--------------------patterns----------------------------------------##
# n = int(input('How many rows do u need: '))
# for i in range(1,n+1):
#     for j in range(i,n+1):
#         print(j,' ', end="")
#     print()
# ###---------------------------------------------------------------------##

# ##--------------------patterns----------------------------------------##

# a=['A','B','C','D']
# b=['P','Q','R']
# i=0
# for i in range(4):
#     print(a[0:i+1] + b[i:])

# ###---------------------------------------------------------------------##

# li='ABCD'
# lj='PQR'
# for i in range(4):
#     chi=li[0:i+1:]
#     chj=lj[i::]
#     print(chi+chj)

# #------------------------------------------------------------------------#
## ------we want only first occurance num which id divisible by 5- else print not found------#
##------- we can use 'else' clause for 'for' loop also in python surprisingly---------#
# nums = [12,13,14,15,16]

# for num in nums:

#     if num % 5 == 0:
#         print(num)
#         break
# else:
#     print("not found")

#-------------------------------------------------------------------#
# num = 97

# for i in range(2,num//2):
#     if num%i == 0:
#         print('Not prime')
#         break
# else:
#     print('Prime')

###---------------------------------------------------------------##


