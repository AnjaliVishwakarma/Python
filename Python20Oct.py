"""Python: OOPS"""
"""
Inheritance:
"""

#Single Level Inheritance
# class C1:
#     def __init__(self):
#         self.a=1
#         self.b=2
#     def showData(self):
#         print("I am in Class C1")
# class C2(C1):
#     def __init__(self):
#         self.c=3
#         self.d=4
#         super().__init__()
# ob=C2()
# print(ob.a,ob.b,ob.c,ob.d)
# ob.showData()


# #Multi Level Inheritance
# class C1:
#     def __init__(self):
#         self.a=1
#         self.b=2
#     def showData(self):
#         print("I am in Class C1")
# class C2(C1):
#     def __init__(self):
#         self.c=3
#         self.d=4
#         super().__init__()
# class C3(C2):
#     def __init__(self):
#         self.e=5
#         self.f=6
#         super().__init__()
# ob=C3()     #6 Variables, ob=1000, ob.__init__()
# print(ob.a,ob.b,ob.c,ob.d,ob.e,ob.f)
# ob.showData()

# #Hierarchichal Inheritance
# class C1:
#     def __init__(self):
#         self.a=1
#         self.b=2
#     def showData(self):
#         print("I am in Class C1")
# class C2(C1):
#     def __init__(self):
#         self.c=3
#         self.d=4
#         super().__init__()
#     def showData(self):
#         print("I am in Class C2")
# class C3(C1):
#     def __init__(self):
#         self.e=5
#         self.f=6
#         super().__init__()
#     def showData(self):
#         print("I am in Class C3")
# class C4(C1):
#     def __init__(self):
#         self.g=7
#         self.h=8
#         super().__init__()
#     def showData(self):
#         print("I am in Class C4")
#
# ob=C4()
# print(ob.a,ob.b,ob.g,ob.h)
# ob.showData()


# #Multiple Inheritance: One Child, Multiple Parents
# class C1:
#     def __init__(self):
#         self.a=1
#         self.b=2
#     # def showData(self):
#     #     print("I am in Class C1")
# class C2:
#     def __init__(self):
#         self.c=3
#         self.d=4
#     # def showData(self):
#     #     print("I am in Class C2")
# class C3:
#     def __init__(self):
#         self.e=5
#         self.f=6
#     def showData(self):
#         print("I am in Class C3")
# class C4(C1,C2,C3):     #MRO: Method Resolution Order
#     def __init__(self):
#         self.g=7
#         self.h=8
#         super().__init__()
#         C2.__init__(self)
#         C3.__init__(self)
#     # def showData(self):
#     #     print("I am in Class C4")
# ob=C4()
# print(ob.a,ob.b,ob.c,ob.d,ob.e,ob.f,ob.g,ob.h)
# ob.showData()
"""If showData method is not present in C4, but present
in all 3 parents then which showData method will be called.
In Java, there is no solution for this concern and there
will be an ambiguity that which parent will be given 
priority and which showData method will be called, this
ambiguity is called Diamond Problem in Java, so in Java
multiple inheritance is not possible directly.
But in Python, a solution to this problem is made ie
MRO: Method Resolution Order is designed.
"""



# #New Program
# L1=[2,3,4]
# L1.pop()
# print(L1)
# L1=[2,3,4]
# list.pop(L1)
# print(L1)

# Single Level Inheritance
# class C1:
#     def __init__(self):
#         self.a=1
#         self.b=2
#     def showData(self):
#         print("I am in Class C1")
# class C2(C1):
#     def __init__(self):
#         self.c=3
#         self.d=4
#         super().__init__()
#     def showData(self):
#         print("I am in Class C2")
# ob=C2()
# print(ob.a,ob.b,ob.c,ob.d)
# ob.showData()
# C1.showData(ob)


# # Single Level Inheritance
# class C1:
#     def __init__(self):
#         self.a=1
#         self.b=2
#     def showData(self):
#         print("I am in Class C1")
# class C2(C1):
#     def __init__(self):
#         self.c=3
#         self.d=4
#         super().__init__()
#     def showData(self):
#         print("I am in Class C2")
#         C1.showData(self)# super().showData()
# ob=C2()
# print(ob.a,ob.b,ob.c,ob.d)
# ob.showData()

# #Hybrid Inheritance 1
# class C1:
#     def __init__(self):
#         self.a=1
#         self.b=2
#     def showData(self):
#         print("I am in Class C1")
# class C2(C1):
#     def __init__(self):
#         self.c=3
#         self.d=4
#         super().__init__()
#     # def showData(self):
#     #     print("I am in Class C2")
# class C3(C1):
#     def __init__(self):
#         self.e=5
#         self.f=6
#         super().__init__()
#     def showData(self):
#         print("I am in Class C3")
# class C4(C2,C3):
#     def __init__(self):
#         self.g=7
#         self.h=8
#         super().__init__()
#         C3.__init__(self)
#     # def showData(self):
#     #     print("I am in Class C4")
# ob=C4()
# print(ob.a,ob.b,ob.c,ob.d,ob.e,ob.f,ob.g,ob.h)
# ob.showData()

# #Hybrid Inheritance 2
# class C1:
#     def __init__(self):
#         self.a=1
#         self.b=2
#     def showData(self):
#         print("I am in Class C1")
# class C2(C1):
#     def __init__(self):
#         self.c=3
#         self.d=4
#         super().__init__()
#     # def showData(self):
#     #     print("I am in Class C2")
# class C3:
#     def __init__(self):
#         self.e=5
#         self.f=6
#     def showData(self):
#         print("I am in Class C3")
# class C4(C2,C3):
#     def __init__(self):
#         self.g=7
#         self.h=8
#         super().__init__()
#         C3.__init__(self)
#     # def showData(self):
#     #     print("I am in Class C4")
# ob=C4()
# print(ob.a,ob.b,ob.c,ob.d,ob.e,ob.f,ob.g,ob.h)
# ob.showData()
# print(C4.__mro__)

# #New Program
# L1=[2,3,4]
# print(L1.__sizeof__())
#
# s="cetpa"
# print(s.__sizeof__())
# print(str.__mro__)

"""
In Python every predefined and user defined class 
has a common parent ie object class. 
In Python there is a predefined variable named as
__mro__ is defined inside object class. 
mro stands for Method Resolution Order through which
we can find the preference is given to which method,
in case we have methods with same names in a parent
child architecture (Group of classes). Will tell us
the priority of methods called.
"""

"""
Employee Resource Planning: Employee
Director: id,name,age,mob,share
Manager: id,name,age,mob,salary,area
Trainer: id,name,age,mob,salary,subject
"""

"""
set and frozenset
set: Collection of heterogeneous data type. set is
mutable in nature. set can have only unique elements.
set is unordered collection of data
Syntax:
var={Comma separated elements}
"""
# s={22,33,55,76,54,33}
# print(s)

# #New Program
# s={22,55,76,54,33}
# L1=list(s)
# print(L1)
# L1.sort(reverse=True)
# print(L1)

# #New Program
# L1=[22,33,44,55,23,45,89,20,30,44,55,23,22]
# s=set(L1)
# print(s)
# L1=list(s)
# print(L1)

# #New Program
# s1={22,33,44,55,66,77}
# s2={55,66,77,88,99}
# r1=s1.union(s2)
# print(r1)
# r2=s1.intersection(s2)
# print(r2)


"""Frozenset:
Collection of heterogeneous data type. frozenset is
immutable in nature. frozenset can have only unique elements.
frozenset is unordered collection of data
Syntax:
var=frozenset({22,33,55,22,33})

Elements of set and frozenset can't be through index
"""
# var=frozenset({22,33,55,22,33})
# print(var)
# print(type(var))

# #New Program
# s={22,33,44,77}
# print(id(s))
# s.add(99)
# print(s)
# s.remove(22)
# print(s)
# print(id(s))

"""

"""
# s=input("Enter Input:")
# print(s)



















