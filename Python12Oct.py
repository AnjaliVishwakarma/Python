"""Python
Assignment: Update CMS
1. Fields: cus name, id, age,mob,email,address,city,state,
pin, gender
2. Add Customer, search,delete,modify,display all..
3. Once we add a new customer, then firstly to cross
check that id is not duplicate
4. add customer: check age,mob,id should be in correct
format
5. Search Cust: Search by id, search by mob, search by
email, search by name...
6. Modify cust...
7. Delete Cust: delete by id or by mob, or by email
8. Search, modify,delete: Firstly Check whether id exists
or not


github: vcs: Version Control Software.

"""

"""OOPS: Object Oriented Programming Language
Class: 1. Collection of Attributes and behaviour.
        2. Collection of Data Members and Member Functions.
        3. Class is a Collection of Variables and Methods.
        4. Class is a user defined data type or a data 
        type.
Syntax:
class Class_Name:
    Variables and methods
    
Object: 1. Object is an Instance of a Class
        2. We can access class properties by using Object
        3. Object is the Real Time Entity which is holding
        memory.
Syntax:
object_name=Class_Name()
or
object_name=Class_Name(Arguments)

To create Methods inside Class:
class Class_Name:
    def function_name(arguments):
        Block of Statement
        
Syntax to call a method:
object_name.method_name(arguments)
While calling if there are n arguments passed in actual
then there should be n+1 arguments in formal parameters.
and first argument will be 'self'. Object will be passed
to self while calling a method.


"""
# class MyClass:
#     pass
#
# ob=MyClass()
# print(type(ob))
# print(ob)


# #New Program
# L1=[2,3,4]
# L2=[7,8,9]
# L1.append(5)
# print(L1)
#
# L1.sort()

# # New Program
# class C1:
#     def func1(self,a,b):
#         print(self,a,b)
#     def func2(t,a):
#         print(t,a)
# ob=C1() #Object of C1 Class
# print(ob)
# ob.func1(5,"abc")   #self=ob, a=5,b="abc"
# ob.func2(77)    #t=ob, a=77

# #New Program
# L1=[2,3,4]
# L1.append(55)

# #New Program
# L1=[22,33,44]
# L2=[22,33,44]
# print(id(L1),id(L2))

# #New Program
# L1=[22,33,44]
# print(id(L1))
# L1=[22,33,44]
# print(id(L1))


# #New Program
# class C1:
#     pass
# ob1=C1()            #Ob1 address 1000
# print(ob1)
# ob1=C1()            #Ob1 address 2000, 1000 address freed
#                     #by Garbage Collector
# print(ob1)
# ob2=C1()
# print(ob2)

# #New Program
# x=5
# del x
# print(x)    #Error

# #New Program
# x=5
# del(x)
# print(x)    #Error

# #New Program
# class C1:
#     def add(self,a,b):
#         r=a+b
#         return r
#
# ob=C1()
# s=ob.add(5,7)     #Inappropriate Approach
# print(s)

"""Object inside class is self
Constructor: Is a Method inside class which is auto-
matically called every time we create a new object.
In Python the name of constructor is fixed ie __init__

Object or user defined data types ie user defined 
classes are mutable in nature.
"""
# class C1:
#     def __init__(self):
#         print("CETPA")
#
# ob1=C1()    #ob1.__init__()
# ob2=C1()
# ob3=C1()

# #New Program
# class C1:
#     def __init__(self):
#         print("CETPA")
#
# ob1=C1()    #ob1.__init__()
# ob2=C1()
# ob3=C1()

# #New Program
# class C1:
#     def __init__(self):
#         print(self)
# ob1=C1()    #ob1.__init__()
# ob2=C1()    #ob1.__init__()

# # #New Program
# # x=5
# # print(x,type(x))
# # y=int()
# # print(y,type(y))
#
#
# #New Program
# class C1:
#     def __init__(self):
#         self.a=5
#         self.b=10
#
# ob=C1()     #ob.__init__()
# print(ob.a,ob.b)
# # print(self)   #Error

# #New Program
# class Customer:
#     def __init__(self):
#         self.id=0
#         self.name=0
#         self.age=0
#         self.mob=0
# ob=Customer()   #ob address 1000, ob.__init__()
# print(ob.id,ob.name,ob.age,ob.mob)

# #New Program
# class C1:
#     def method1(self):
#         self.a=0
#         self.b=0
#
# ob=C1()
# print(ob.a,ob.b)    #Error

# #New Program
# class C1:
#     def method1(self):
#         self.a=0
#         self.b=0
#
# ob=C1()
# ob.method1()
# print(ob.a,ob.b)

# #New Program
# class Customer:
#     def __init__(self):
#         self.id=0
#         self.name=0
#         self.age=0
#         self.mob=0
# cus1=Customer()
# cus2=Customer() #cus2.__init__()
# cus1.id=10
# cus1.name="Vikas"
# cus1.age=39
# cus1.mob=1234
# print(cus1.id,cus1.name,cus1.age,cus1.mob)
# print(cus2.id,cus2.name,cus2.age,cus2.mob)

#New Program
class C1:
    def __init__(self):
        self.a=0
        self.b=0

    def func1(self):
        self.a=1
        self.b=2
ob1=C1()    #Ob1 address 1000, ob1.__init__()
ob2=C1()    #Ob2 address 2000, ob2.__init__()
ob1.func1()
print(ob1.a,ob1.b)
print(ob2.a,ob2.b)


