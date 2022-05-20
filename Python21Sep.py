"""Python Continue"""
"Starting Shortly, be on standby"
#Calci
# import math
# choice=input("Enter Choice +, -, sin, log, fact:")
# no1=int(input("Enter First No:"))
# if(choice=="sin"):
#     res=math.sin(no1)
#     print("Result:",res)
# elif(choice=="fact"):
#     res=math.factorial(no1)
#     print("Result:",res)
# else:
#     no2=int(input("Enter Second No:"))
#     if(choice=="+"):
#         res = no1+no2
#         print("Result:", res)
#     elif(choice=="-"):
#         res = no1-no2
#         print("Result:", res)
#     elif(choice=="log"):
#         res = math.log(no1,no2)
#         print("Result:", res)
#     else:
#         print("Incorrect Choice")

"""
Biggest of 3 Nos:
"""
# no1=int(input("Enter First No:"))
# no2=int(input("Enter Second No:"))
# no3=int(input("Enter Third No:"))
# if(no1>no2):
#     if(no1>no3):
#         print("The Biggest No is:",no1)
#     else:
#         print("The Biggest No is:",no3)
# else:
#     if(no2>no3):
#         print("The Biggest No is:",no2)
#     else:
#         print("The Biggest No is:",no3)

"""
Stackoverflow:

HackerRank: As a Fresher better to start.
HackerEarth: Next Level 
"""

"""
    
Keyword: Predefined words. Ex: if,elif,else,def...

Identifiers: User Defined Words
variable name, function name, class name...
Rules for Identifiers
Valid Identifiers: Can be collection of
    1. English Alphabets (a to z or A to Z)
    2. Numbers (0 to 9)
    3. Special Symbol: Only underscore
InValid Identifiers: 
    1. First Character should be not start with number
    2. No other special symbol allowed other than underscore
    3. Keywords can't be used as identifiers

a42_=8      #Valid Identifier
print(a42_)

vikas=8      #Valid Identifier
print(vikas)

vikas kalra=8      #InValid Identifier
print(vikas kalra)

Python is Case Sensitive Language
a=5
A=8
print(a,A)

User defined Functions:

Syntax to create functions:
def function_name(arguments):#arguments: Formal parameters
    Block of Code
    return argument (optional)

Syntax to Call a Function:
    function_name(arguments):#arguments: Actual parameters
    var_name=function_name(arguments)

"""
#New Program
# a=5
# A=8
# print(a,A)

"""
Layered Architecture:
At top there are different types of layers in the
program. The most popular 2 layers in layered 
architecture at top level are:
1. Presentation Layer (PL): Responsible for user 
interaction
2. Business Logic Layer (BLL): Responsible for 
implementing the actual functionality of the code 
ie responsible for writing the business logic.

Formal and actual parameters names may be same or
different
"""
# #New Program
# def add(a,b):
#     s=a+b
#     return s
# a,b=5,7
# r=add(a,b)      #r=a+b
# print(r)

# #New Program: Sum of Inputs
# def add(u,v):   #Addition of arguments
#     s=u+v
#     return s        #return u+v
#
# a=int(input("Enter First No:")) #a=5
# b=int(input("Enter Second No:"))    #b=7
# r=add(a,b)                #r=a+b
# print("Result:",r)
# print(add(a,b))

# #New Program
# def add(u,v):
#     s=u+v
#     return s
#
# a,b,c,d=2,3,4,5
# r1=add(a,b)
# print(r1)
# r2=add(c,d)
# print(r2)

# #New Program
# def add(u,v):
#     s=u+v
#     return s
# a,b=2,3
# r1=add(a)   #Error
# print(r1)

"""The functions which do not return any value, then
they by default return None value.
"""
# def myfunc(a,b):
#     s=a+b
#
# r=myfunc(5,7)
# print(r)
# print(type(r))

# #New Program
# a=input("Enter Any Data:")

# #New Program
# a=print("CETPA")
# print(a)

# #New Program
# print(print("CETPA"))

# #New Program
# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
#
# a,b=5,7
# print(add(a,b))
# print(sub(a,b))

# #New Program: Addition of 2 Nos
# #BLL: Business Logic Layer
# def add(a,b):
#     r=a+b
#     return r
#
# #Presentation Layer
# no1=int(input("Enter First No:"))
# no2=int(input("Enter Second No:"))
# res=add(no1,no2)
# print("Result:",res)

# #New Program: Addition of 2 Nos
# #Mixing PL and BLL: Not a good approach
# no1=int(input("Enter First No:"))
# no2=int(input("Enter Second No:"))
# def add(a,b):
#     r=a+b
#     return r
# res=add(no1,no2)
# print("Result:",res)

"""
Firstly BLL and then PL 
"""
# a,b=5,7
# s=add(a,b)  #Error
# print(s)
# def add(a,b):
#     return a+b

# #New Program
# a,b=5,7
# def add(a,b):
#     return a+b
# s=add(a,b)
# print(s)

"""Functions are never executed on its own.
Functions are always executed once they are called
ie Function body executes once we call but function
definition is created on its own.
"""

#New Progam:
# #Business Logic Layer
# def add(a,b):       #1,
#     s=a+b           #5
#     return s        #6
# #Presentation Layer
# no1=int(input("Enter First No:"))   #2
# no2=int(input("Enter Second No:"))  #3
# res=add(no1,no2)                    #4, 7
# print("Result:",res)                #8

# #New Program
# #Mixing PL and BLL
# def add(a,b):       #1,
#     s=a+b           #5
#     print(s)
#
# no1=int(input("Enter First No:"))   #2
# no2=int(input("Enter Second No:"))  #3
# add(no1,no2)                    #4, 7


"""First Kasam: Being CETPA student and not a Student
of any Tom, Dick and Harry Institute, we will always
use input and print function in Presentation Layer."""









