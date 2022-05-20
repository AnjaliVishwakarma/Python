"Python Continue"
"""Python Supports Dynamic Data Type Definition
& Dynamic Memory Allocation

Dynamic Data Type Definition: Data type definition at
run time. In Python, Data types are implicitly defined.

Dynamic Memory Allocation: Memory Allocation at Run Time

Data Types: Designed to distinguish different kinds of data
by the machine.

Two Types:
Single Element/Single Valued Data Type:
int,float,bool,NoneType
a=5
a=2.5
a=True
a=False
a=NoneType, None


Multi Element/Multi Valued/Iterator/Sequence/Collection
Can have 0,1 or more elements
str
list
tuple
dict
set
frozenset


a="CETPA"
a=[2,3,4.5,"abc"]


C Lang/Java: Compiler Based Languages: Firstly program
is compiled: Errors in the Program are checked, Data types
definition, memory allocate all at compile time.

Python: Interpreter based language: Run Time execution...

C Lang:
1. At compile time, require memory is decided ex 2 bytes
2. At compile time, that much free memory is searched in RAM
3. At compile time, that memory will be freezed and 
variable will start pointing to that memory location
a=5
1. Calculate: It require 2 bytes
2. Search in RAM, where 2 bytes are free say at 1000 location
3. That location is freezed and a start pointing to that
location.
At run time in C Lang:
a=5   ; 5 will be stored at 1000 location
4.
a=7   ; 7 will be overwritten at 1000 location 

int a; 
a=5;
a=7;

4 Digits Decimal No: 9999
16 Bits Biggest Value: 1111111111111111: 2 ** 16 - 1=65535

Variables are saved in RAM. 

In Python:
a=5
1. Firstly it will be checked, how much memory is required
to store 5 value. 
2. It will be searched in RAM where that much memory is
free to store 5. Say location is 1000
3. That memory will be freezed/occupied
4. Value 5 will be stored at that location. 5 will be
stored at 1000 location
5. a will point to 1000 location

a=7
Again all above steps will be repeated and 7 will be
stored at a new location say at 2000 location.
Dynamic Memory Allocation.

Now it takes too much time to run a program in interpreter
based language than a compiler based language.

Now what's the benefit of using Interpreter based language
or benefit of Dynamic Memory Allocation:
1. Dynamic Data Type definition is achieved through Dynamic 
Memory Allocation
a=5 #5 stored at 1000 location.
a=2.5   #2.5 will be stored at 2000 location
a="CETPA"   #"CETPA" will be stored at next free location 3000
2. There is no value limitations in Python.


"""

# a=5
# print(a)
# print(type(a))
# a=2.5
# print(a)
# print(type(a))

# #New Program
# a=100
# print(a)
# print(type(a))
# a=555555555555555555555555555555555555555555
# print(a)
# print(type(a))

# #New Program
# a=5
# a=7
# print(a)
# a=9
# a=11

# #New Program
# a=5
# print(id(a))
# a=7
# print(id(a))

"""In Python, In Dynamic Memory Allocation: Whenever
we assign a new value to a variable then it is stored
at a new address. The previous location in case if
not pointed by any other variable then it is free by
the garbage collection"""

# a=5         #5 at 1000 location, a refering to 1000
# print(id(a))
# b=a         #Call be reference: b will also starts refering to 1000
# print(id(b))

# #New Program
# a=5         #5 at 1000 location and a refer to 1000
# print(a)
# a=7         #7 at 2000 location, a refer to 200
#             #1000 location is not referred by any varialbe
#             #So it will be freed by garbage collector
# print(a)

#New Program
"""Whenever we store a new value it is always stored 
at new location."""

# #New Program
# a=5     #a: 1000 location
# b=a     #b: 1000 location
# a=7     #a: 2000 location
# print(a)
# print(b)

#New Program
# """4. Print the Nos 1 to 5 at screen with a gap of
# two lines in between using 5 print  statements"""
# print(1,end="\n\n")
# print(2,end="\n\n")
# print(3,end="\n\n")
# print(4,end="\n\n")
# print(5,end="\n\n")

# """4. Print the Nos 1 to 5 at screen with a gap of
# # two lines in between using single print  statements"""
# print(1,2,3,4,5,sep="\n\n")


# print(range(1,5))

# x=input("Enter Any Data:")
# print(type(x))


"""No Practise No Learning
"""



