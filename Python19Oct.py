"Python"
# namelist=["Vikas","Anil","Amit"]
# i=2     #id=30, name="Sonu"
# name="Sonu"
# namelist[i]=name

"""OOPS Properties
1. Abstraction
2. Encapsulation
3. Inheritance
4. Polymorphism
"""

"""
Abstraction: Hiding the background details

Encapsulation: Binding the data and methods in a single unit.

Inheritance: Inheriting the properties of one class
                from another class. Properties means
                variables and methods
            To make the code reusable
                
Polymorphism: Many Forms: Same functions name 
Overloading: Same function name with different signatures
             in same class. Python doesn't support overloading
Overriding: Same function name with same signature in
            derived class. But it also supports different
            signatures.
 
"""
# L1=["abc","def","ghi"]
# L1.upper()      #Error
# print(L1)

# #New Program
# class C1:
#     def showData(self):
#         print("CETPA")
# class C2:
#     pass
# ob=C2()
# ob.showData()   #Error

# #New Program
# class C1:
#     def showData(self):
#         print("CETPA")
# class C2(C1):   #C2 Child, C1 Parent
#     pass
# ob=C2()
# ob.showData()


# #New Program
# class C1:
#     def __init__(self):
#         self.a=1
#         self.b=2
#     def showData(self):
#         print("CETPA")
# class C2(C1):   #C2 Child, C1 Parent
#     pass
# ob=C2()
# print(ob.a,ob.b)
# ob.showData()

# #New Program
# class C1:
#     def showData(self):
#         print("I am in Class C1")
# class C2(C1):
#     def showData(self): #Overriding
#         print("I am in Class C2")
# ob=C2()
# ob.showData()

"""To achieve inheritance:
    1. Mention parent class name(s) in bracket of 
    child class name
    2. Call parent(s) constructor inside child constructor 
    """
# #New Program
# class C1:
#     def __init__(self):
#         self.a=1
#         self.b=2
# class C2(C1):
#     def __init__(self):
#         self.c=3
#         self.d=4
#         super().__init__()
# ob=C2()     #ob.__init__()  #ob address 1000
# print(ob.a,ob.b,ob.c,ob.d)

# #New Program
# class C1:
#     def __init__(self):
#         self.a=1
#         self.b=2
# class C2(C1):
#     def __init__(self):
#         self.a=3
#         self.b=4
#         super().__init__()
# ob=C2()     #ob.__init__()  #ob address 1000
# print(ob.a,ob.b)


# #New Program
# class C1:
#     def __init__(self):
#         self.a=1
#         self.b=2
#     def showData(self):
#         print("CETPA")
# class C2(C1):
#     def __init__(self):
#         self.c=3
#         self.d=4
#         super().__init__()
# ob=C2()     #ob.__init__()  #ob address 1000
# print(ob.a,ob.b,ob.c,ob.d)
# ob.showData()

"""
Parent/Base/Super
Child/Derived/Sub

Types of Inheritance
1. Single Level Inheritance: One Parent and One Child
2. Multi Level Inheritance: 
3. Hierarchical  Inheritance
4. Multiple Inheritance
5. Hybrid Inheritance
"""
















# #New Program
# class C1:
#     def __init__(self):
#         self.a=1
#         self.b=2
#     def showData(self):
#         print("CETPA")
# class C2(C1):   #C2 Child, C1 Parent
#     def __init__(self):
#         self.c=3
#         self.d=4
# ob=C2()
# print(ob.a,ob.b,ob.c,ob.d)  #Error
# ob.showData()

# #New Program: Python does not support overloading
# def add(a,b):
#     return a+b
# def add(a,b,c):
#     return a+b+c
#
# s1=add(2,3,4)
# print(s1)
# s2=add(2,3)
# print(s2)   #Error
