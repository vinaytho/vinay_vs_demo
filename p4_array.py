'''
from array import *
n = int(input("Enter the len of array u want: "))

arr = array('i',[])

for i in range(n):
    k = int(input("Enter the array input value: "))
    arr.append(k)
print(arr)

val = int(input("Enter the value to find the index: "))
k = 0
for m in arr:
    if m==val:
        print(arr[k])
        print(k)
        break
    k +=1

print(arr.index(val))

'''
from re import I
from numpy import *
#-----------------------------------------#
'''

arr = array([12,34,56,78])
print(arr)
print(arr.dtype)
arr1 = array([12,34,56,78.0])
print(arr1)
print(arr1.dtype)
arr2 = array([12,34,56,78],float)
print(arr2)
print(arr2.dtype)

'''
#-------------------------------------------#
'''
arr = linspace(0,15,16)
print(arr)
arr1=linspace(0,15,20)
print(arr1)
arr2 = linspace(0,25)       #by default it breaks into 50 parts
print(arr2)
'''
#--------------------------------------------#
'''
arr = arange(5)
print(arr)
arr1 = arange(1,100,20)
print(arr1)
arr2 = arange(1,20)
print(arr2) 
'''
#------------------------------------------#
'''
def person(name, **data):

    print(name)
    print(data)
    print(data.items())
    for i,j in data.items():
        print(i,j)

person('Vinay',age=28,city='Vizag',mob=944108)
'''
#-------------------------------------------------------#
'''
a = 10
print(id(a))

def somefun():
    a = 5
    print("in fun - :",a)
    print(id(a))

    x = globals()['a']
    print(x)
    print(id(x))
    globals()['a'] = 20
    print


somefun()
print('outside fun - ',a)
print(__file__)

'''
#----------------------------------------------#
'''
a=[]

num=int(input('Length of array: '))
for i in range(num):
    num=int(input('Enter value of array: '))
    a.append(num)

print(a) 

def cnt(lst):
    even = 0
    odd = 0

    for i in lst:
        if i%2 == 0:
            even +=1
        else:
            odd +=1
    return even,odd

even,odd = cnt(a)

print(f'Even: {even} and Odd: {odd}')
'''
#----------------------------------------------#
##Fabinocci
'''
a=0
b=1
num=int(input('Length of fabinocci: '))
i = 0
print(a)
print(b)
while i<num-2:
    temp = a
    a = b
    b = temp + a
    print(b)
    i+=1
'''
#------------------------------------------------#
'''
def fab(num):
    a = 0
    b = 1

    if num<0:
        print('Negative length is invalid')
    elif num == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,num):
            c = a
            a = b
            b = c + a
            print(b)

num=int(input('Length of fabinocci: '))
fab(num)
'''
#--------------------------------------------------#
'''
def fabUpto(num):
    a = 0
    b = 1

    if num<0:
        print('Negative length is invalid')
    elif num == 0:
        print(a)
    else:
        print(a)
        print(b)
        while b <= num:
            c = a
            a = b
            b = c + a
            if b<=num:
                print(b)


num=int(input('Enter max number of fabinocci: '))
fabUpto(num)
'''
#========================================================

##factorial

# def fact(x):
#     f=1
#     for i in range(1,x+1):
#         f *=i
    
#     return f

# x = 4
# result = fact(x)
# print(result)

# ###---------------------------------------##
# ## - recurtion  - a function calling itself
# import sys
# sys.setrecursionlimit(200)

# print(sys.getrecursionlimit())
# i = 0
 
# def greet():
#     global i 
#     i +=1
#     print('Hello', i)
#     greet()

# greet()

# #------------------------------------------------#

# ##factorial using recursion

# def fact(n):
#     if n==0:
#         return 1
#     return n*fact(n-1)


# result = fact(3)
# print(result)
# #----------------------------------------#

# ##---lambda functions are anonymous functions without names and it should contain only one expression
##like a*a, a*b,etc., it can take n number of inputs but only holds one expression
# f = lambda a: a*a
# print(f(4))

#---------------------------------------------#
from functools import reduce


nums = [2,3,4,5,6,7,8,9,3,54,6,7,8,9,5,4]

evens = list(filter(lambda n: n%2==0,nums))    
print(evens)

doubles = list(map(lambda n: n*2,evens))
print(doubles)

sum = reduce(lambda a,b : a+b, doubles)
print(sum)

a=list(map(lambda n: n*2,nums))
print(a)

fact=reduce(lambda n,m: n*m, range(1,6))
print(fact)


