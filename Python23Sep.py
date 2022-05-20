"""Good Morning Everyone"""

"""Data Types:
Single Element:
int,float,complex,bool,NoneType

Multi Element/Iterators
str,list,tuple,dict,set,frozenset

String Collection of Homogeneous data type ie characters

List is a collection of Heterogeneous data type.
"""
# s="CETPA"   #Index: 0 to 4
# print(s[0])
# print(s[1])
# print(s[4])
# print(len(s))

# #New Program
# L1=[22,33.4,55,88,"CETPA"]  #index 0 to 4
# print(L1[4])
# print(L1[4][2])
# a=L1[4]
# print(a[2])

# #New Program
# L1=[[2,3,4],[5,6,7]]    #index 0 and 1. 2x3. 2-D list
# print(L1[1])        #[5, 6, 7]
# print(len(L1))
# print(L1[1][2])

"""Mutable Types: 
Immutable Types

Saneen: Which can't be modified: Immutable

String is immutable

Variable: Whose value vary in the Program

int,float,complex,bool,NoneType,str,tuple,frozenset all
are immutable data type.

list,dict,set are mutable data type

Mutable: Which can be modified. Can understand it
better ie elements of mutable types can be changed.

Immutable: Which can't be modified.
"""
# s="CETPA"
# print(s)
# s="Welcome"
# print(s)

# #New Program
# x=5         #x address 1000
# print(x,id(x))
# x=7         #x new address say 2000
# print(x,id(x))

# #New Program
# x="CETPA"         #base address 1000
# print(id(x))
# x="Welcome"       #base address 2000
# print(id(x))

# #New Program
# x="CETPA"   #0 to 4
# print(x[0])
# print(x[4])

# #New Program
# x="CETPA"   #0 to 4
# x[1]="M"    #Error: String is immutable in nature

# #New Program
# L1=[22,33,44,55,66]     #L1 base address 1000
# print(id(L1))
# L1="CETPA"              #L1 base address 2000
# print(id(L1))

# #New Program
# L1=[22,33,44,55,66]
# print(id(L1))
# L1[0],L1[1]=99,77
# print(L1)
# print(id(L1))

"""Tuple: Collection of Heterogeneous data type
Tuple is immutable in nature
Syntax: (comma separated elements)
"""
# t=(22,23.5,"CETPA",True)
# print(t)
# print(type(t))

# #New Program
# t=(2,3,4,5,6)
# t[0]=8      #Error: Tuple is immutable
# print(t)

"""All variables in Python are of ref type. If we 
assign one variable to another then their addresses
are copied

Divesh
"""
# a=5     #a address 1000
# b=a     #b address 1000
# print(id(a),id(b))
# a=6     #a address 2000, b address 1000

"""If we modify/increase/decrease the elements of 
list the base address of list won't change"""

# #New Program
# L1=[22,33,44,55]
# L1[1]=88
# print(L1)

# #New Program
# a=5
# b=a
# a=6
# print(b)
# L1=[22,33,44]       #L1 base address 1000
# print(id(L1))
# L2=L1               #L2 base address 1000
# print(id(L2))
# L1[0]=66            #L1, L2 base address 1000
# print(L2)   #[22,33,44]
# print(id(L1),id(L2))
# L1.append(55)
# print(L1,L2)
# print(id(L1),id(L2))


# #New Program
# L1=[22,33,44]
# L2=L1
# L3=L1.copy()
# print(id(L1),id(L2),id(L3))
# print(L1,L2,L3)

"""tuple is generally used to share data between
PL and BLL"""
# def func1(L2):  #L2 address 1000
#     L2[0]=66    #L2 address 1000
#
# L1=[22,33,44]       #L1 base address 1000
# func1(L1)   #L2=L1
# print(L1)       #[22,33,44]

# #New Program
# def func1(L2):  #L2 address 1000
#     L2=[11,44]    #L2 address 2000
#
# L1=[22,33,44]       #L1 base address 1000
# func1(L1)   #L2=L1
# print(L1)       #[22,33,44]

# #New Program
# L1=[22,33,44]
# t=tuple(L1)
# print(t)
# s="cetpa"
# L2=list(s)
# print(L2)

# #New Program
# s=input("Enter 5 No:")
# L=s.split()
# print(L)


# #New Program
# L1=[20,30,40]       #Base address 1000-1049
# print(id(L1))
# a=55                #a address 1050
# L1.append(5000000000000000000000000000000)
# print(id(L1))
# print(L1)

"""To store one reference/address in Python, it takes
8 bytes:64 bits"""
# #New Program
# L1=[22,"Welcome",45.7777777777777777]
# print(L1[2])

# """Java is more popular than Python
# Java Script is the World's most popular language,
# highly used.
# """




