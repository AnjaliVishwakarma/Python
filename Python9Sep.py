"""Python Programming"""
"""IDE: Integrated Development Environment
1. IDLE: Integrated Development Learning Environment
This is a product of python.org
2. Pycharm: Very Popular IDE due to: Its 
recommendation is very fast.
3. Anaconda Environment:
    1. Jupyter Notebook
    2. Spyder IDE
4. vscode: getting popular: Microsoft Product
5. Google Colab. Fast Applications
6. Visual Studio
.
.

Pycharm: Google type: Pycharm download
Virtual Environment Setup: Checkbox: Check



"""

"""
Comments:
Official way to use the comments in program is: #
Python officialy supports single line comments

But there are Jugaads to write multiline comments
ie by using triple quotes

Single Line Comments: # or single quotes or 
                        double quotes
                        
Multi Line Comments: Triple Single Quotes or
                    Triple Double Quotes
"""

# print("CETPA")      #This statement is going to print
                    #CETPA


"CETPA"
'cetpa'

"""Welcome to CETPA.
Award Wining Training Company
Awarded by Chetan Bhagat, Soha Ali Khan..."""

'''Welcome to CETPA.
Award Wining Training Company
Awarded by Chetan Bhagat, Soha Ali Khan...'''

"""
Version 1 of print function: 
print(values,variables,expressions,conditions,functions...)

Syntax:
print(comma separated arguments)

Whenever print function executes, it takes the cursor
to next line at the end of execution of print function
"""
# #New Program
# a=5
# b=3.5
# c="cetpa"
# print(a,b,c)

# #New Program
# a=5
# b=3.5
# c="cetpa"
# print(a,b,c,67,77,99.5,"CETPA",a+b,a==b)

"""There is no negative marking in our class"""

#New Program: Cntrl + /
# a=7
# b=2.0
# print(a+b)

# #New Program
# a,b,c,d,e=2,3,4,5,6
# print(a,b,c,d,e)
# print("CETPA")

"""
Version 2 of print function:
We are already aware now that whenever we run print
functions, there is automatically a space is printed in
between the arguments and after the execution of print
function, cursor automatically moves to next line

\ is an escape character
\n: Escape Character: New Line Character
\t: Tab Character

First extension of print function:
print(Arguments,sep=" ",end="\n")

a,b,c=5,7,9
print(a,b,c)    #print(a sep b sep c end)
By default sep is having space, end is having new line character
But if we want we can intentionally change these values. 
"""
# #New Program
# a,b,c,d,e=5,7,9,11,13
# print(a,b,c)
# print(d,e)

# #New Program
# a,b,c,d,e=5,7,9,11,13
# print(a,b,c,sep="*",end="\n\n")     #a sep b sep c end
# print(d,e)

# #New Program
# a,b,c,d,e=5,7,9,11,13
# print(a,b,c,sep="CETPA",end="")     #a sep b sep c end
# print(d,e)

# #New Program
# x="Welcome"
# print(x)
# x="Wel\ncome"
# print(x)
# x="c\tetpa"
# print(x)

# #New Program
# print("*")
# print("*")
# print("*")

# #New Program
# print("*",end="")
# print("*",end="")
# print("*",end="")
# print("*",end="")

# #New Program
# a,b,c,d,e=2,3,4,5,6
# print(a,b,c,sep="#",end="CETPA")
# print(d,e)

# #New Program
# a,b,c,d,e,f=2,3,4,5,6,7
# print(a,b,end="*")
# print(c,d,sep="55")
# print(e,sep="#",end="$")
# print(f)

# #New Program
# print("*",end="")
# print("*",end="")
# print("*",end="")
# print("*",end="")

"""For user interaction, we have two basic functions
ie print() and input()
print() to send output on screen
input() to collect/input the data from user

No Practise No Learning
"""

"""
input function
Syntax:
return_var=input("Message for User")
"""
# #New Program
# a=input("Enter Your Name:")
# print(a)

# #New Program
# a=input("Enter First No:")
# b=input("Enter Second No:")
# s=a+b
# print(s)

"""String: 
x="cetpa"
print(x)
"""
#New Program
# x="cetpa"
# print(x)
# x="5"
# print(x)

# # #New Program
# a=5
# b=2.5
# c="5"
# print(type(a))
# print(type(b))
# print(type(c))
# print(a,b,c)

"""Now whenever we interact with the screen, data is
always transferred in forms of strings. In input function
if user pass any value then it will be of string form
Whenever we use + operator on strings then the strings
are concatenated.
"""
# x=input("Enter First No:")
# print(type(x))
# print(x)

# #New Program
# print("Hello"+"World")
# print("5"+"7")

# #New Program
# x=input("Enter First No:")  #x="5"
# y=input("Enter Second No:") #y="7"
# s=x+y
# print(s)

"""Type Casting: To convert one data type to another
data type.
Syntax:
Dest_var=Dest_type(Src_var)
"""
# x="5"
# print(type(x))
# x=int(x)
# print(type(x))
# x=float(x)
# print(type(x))

# #New Program: WAP to add two inputs
# x=input("Enter First No:")
# x=int(x)
# y=int(input("Enter Second No:"))
# s=x+y
# print("Result:",s)

