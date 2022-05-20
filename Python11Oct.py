"""Python Continue"""
"""Function Types
1. Required Argument Function
2. Keyword Argument Function
3. Default Argument Function
4. Variable Length Argument Function
    a. Tuple based: Variable Length Argument Function
    b. Dict based: Variable Length Keyword Argument Function
5. Lambda Function 
"""

"""
1. Required Argument Function: No of arguments and 
sequence of arguments in both formal and actual should
match. Also called Positional Argument Functions
"""
# def sub(a,b):     #formal parameters a,b
#     return a-b
#
# u,v=2,3
# r=sub(u,v)      #Result u-v, Actual parameters u,v
# print(r)


"""
Keyword Argument Function: No. of arguments in formal
and actual parameters should match. While calling,
we specify formal variable=actual variable
"""
#
# def sub(a,b):     #formal parameters a,b
#     return a-b
#
# u,v=2,3
# r=sub(b=v,a=u)      #Result u-v, formal=actual
# print(r)


"""
3. Default Argument Functions: We set the default value
in formal, now its optional to pass these values in 
actual.
"""
# def add(a=5,b=7):
#     return a+b
#
# s1=add(3,4)     #s1=7
# s2=add()        #s2=12
# s3=add(9)       #s3=16
# s4=add(b=30)
# print(s1,s2,s3,s4)

"""
Variable Length Arguments Functions: No of arguments
in actual parameters may vary as per the requirement.
    a. tuple based: Variable Length Arguments Functions
        Python recommend to keep formal variable name
        as *args in this category.
    a. dict based: Variable Length Keyword Arguments Functions
        Python recommend to keep formal variable name
        as *kwargs in this category.

"""
# def myfunc(*t): #Variable length argument function
#     print(t)
# a,b,c,d,e=2,3,4,5,6
# myfunc(a,b) #unpacked variables from actual will be
#             #packed to formal tuple type variable
# myfunc(a,b,c,d)
# myfunc()
# myfunc(a,b,c,d,e)

#New Program
#BLL
# def add(*args):     #args=(4,5,6,7)
#     r=0
#     for e in args:
#         r=r + e
#     return r
#PL
# s1=add(2,3)
# s2=add(4,5,6,7)
# s3=add(1,2,3,4,5,6,7,8)
# print(s1,s2,s3)


# #New Program
# def myFunc(**d):
#     print(d)
#
# u,v=32,44
# myFunc(a=5,b=6,c="abc",d=[22,33])
# myFunc()
# myFunc(m=9,n=u,p=v)


"""Create a Variable Length Keyword argument based add
function.
"""
# a=5;
# b=6;print(a,b)

# #New Program
# def add(**kwargs):  #kwargs={'a':2,'b':3,'c':4,'d':5,'e':6}
#     r=0
#     for e in kwargs.values():   #2,3,4,5,6
#         r=r+e
#     return r
#
# a,b,c,d,e=2,3,4,5,6
# s1=add(a=a,b=b,c=c,d=d,e=e)
# s2=add(m=a,n=b)
# s3=add(a=4,b=5,c=6,d=7)
# print(s1,s2,s3)


"""
Lambda Functions: Single Line Anonymous functions.

Everything in python is designed through class and 
in our program whenever we create something new then
it will be an object of the class.

All variables in Python are of ref type. But some 
variables behaves like value type like we already 
studied: int, float,....list,tuple....Means when we
print them then their value get printed.
Rest will be of ref type

All functions (user defined or predefined) in Python
are the objects of function class and when we print 
them then their address get printed.

Function Pointer: Function Pointer is a variable which
holds the address of a function.

Syntax of Lambda Function Creation:
lambda arguments passed:expression returned
"""
# #New Program
# def add(a,b):
#     return a+b
#
# s=add       #Object of function class, s function pointer
# print(s)
# print(type(s))
# print(add)
# print(type(add))

# #New Program
# def add(a,b):
#     return a+b
# s=add       #s function pointer
# print(add)  #Object of function class
# print(s)
# print(add(2,3))
# print(s(2,3))



# #New Program
# add=lambda a,b:a+b    #add is not the name of lambda function
#                     #but it is a function pointer
# print(add)
# print(add(2,3))

# #New Program
# n=int(input("Enter Any Number:"))
# oddeven=lambda a:a%2
# r=oddeven(n)
# if(r==0):
#     print("Even")
# else:
#     print("Odd")
# #New Program
# a=5
# r='Even' if a%2==0 else 'Odd'
# print(r)
# #New Program
# n=int(input("Enter Any Number:"))
# oddeven=lambda a:'Even' if a%2==0 else 'Odd'
# r=oddeven(n)
# print("The Entered No is:",r)


"""OOPS Tomorrow"""