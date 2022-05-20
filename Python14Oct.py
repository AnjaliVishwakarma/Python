"""Python OOPS"""
# L1=["abc","def"]
# L1.upper()    #AttributeError
# print(L1)

# #New Program
# class C1:
#     def func(self):
#         print("CETPA")
# class C2:
#     pass
# ob=C2()
# ob.func()   #AttributeError

# #New Program
# class C1:
#     class C2:
#         pass


"""
Types of Variables inside Class:
static variable/class variable/shared variable:
Whatever variables we studied before OOPS ie outside
class are all static variables. 
    1. Static variables are common variables for all 
    objects. 
    2. These Variables are directly created inside class
    like local variables are created outside class.
    3. Static variables are accessed through class name
    preferably 

instance variable/object variable: Whatever variables
we studied till now inside class, all were instance
variable. 
    1. Instance variables are different variables
        for different objects.
    2. Instance Variables are created with Object name.
    3. Instance variables can be created outside class
        or inside methods inside class. But Instance
        variables are preferably created inside constructor.
"""
# class C1:
#     a,b=1,2     #Static Variables
#     def __init__(self):
#         self.u=3    #Instance Variable
#         self.v=4    #Instance Variable
#
# ob1=C1()    #ob1.u=3,ob1.v=4, C1.a=1, C1.b=2
# ob2=C1()    #ob2.u=3,ob2.v=4, C1.a=1, C1.b=2
# ob1.u=5
# C1.a=6
# print(ob1.u,ob2.u,C1.a)

# #New Program: Example Static vs Instance Variable
# class C1:
#     a=0
#     def __init__(self):
#         self.b=0
#     def inc(self):
#         C1.a+=1
#         self.b+=1
#         print(C1.a,self.b)
# ob1=C1()    #ob1 address 1000, ob1.b=0, C1.a=0
# ob1.inc()   #C1.a=1, ob1.b=1
# ob2=C1()    #ob2 address 2000, ob2.b=0, C1.a=1
# ob2.inc()   #C1.a=2, ob2.b=1
# ob3=C1()    #ob3 address 3000, ob3.b=0, C1.a=2
# ob3.inc()   #C1.a=3, ob3.b=1
# print(ob1.a)
# print(ob2.a)
# print(ob3.a)


#New Program: Object Counter: Everytime we create an
#object, the count no of that object should be printed
#on screen

# a=5
# print(a=7) #Error
# # print(a+=1) #Error

# #New Program
# class C1:
#     count=0
#     def __init__(self):
#         C1.count+=1
#         print(C1.count)
# ob1=C1()
# ob2=C1()
# ob3=C1()
# ob4=C1()

# #New Program
# count=0
# count+=1
# count+=1
# print(count)

"""
Static Methods vs Instance Methods
Static Methods/Functions: Are like normal functions 
defined outside class. These are created exactly same
as functions outside class but we put extra 
@staticmethod decorator before function creation. 
Static methods are preferably accessed through class 
name.

Instance Methods: Till now whatever methods we created
inside class are instance methods. Instance methods
are called through object name. When we create instance
methods then first argument is taken as self. When
we call instance method then object is passed to self.

Generally developer community prefers to call static 
functions as functions or static functions, and instance
functions as methods or instance methods. To create 

"""
# def func1(a,b):
#     print(a,b)
# class C1:
#     @staticmethod
#     def func2(a,b):     #Static Function
#         print(a,b)
#
# func1(5,7)
# C1.func2(5,7)


# #New Program
# L1=[2,3,4]
# L1.func1()

# #New Program
# class C1:
#     @staticmethod
#     def myPrint():
#         print("CETPA")
#
# C1.myPrint()

"""
05-11-1981
"""

"""CMS: Customer Management System
Add Customer, Search Customer, Delete Customer, Modify Customer
"""
#BLL
class Customer:
    cuslist=[]  #Customer.cuslist=[1000,2000,3000...
    def __init__(self):
        self.id=0
        self.name=""
        self.age=0
        self.mob=0
    def addCustomer(self):  #self.id=10,self.name="Vikas"...
        Customer.cuslist.append(self)
    def searchCustomer(self): #self=8000, self.id=20
        for e in Customer.cuslist:
            if(e.id==self.id):
                self.name=e.name
                self.age=e.age
                self.mob=e.mob



#PL
def showCustomer(cus):
    print("Cust Id:",cus.id,"Cust Name:",cus.name,"Cust Age:",cus.age,"Cust Mob:",cus.mob)
while(1):
    print("1 for Add Cust, 2 for Search Cust")
    print("3 for Delete Cust, 4 for Modify Cust")
    print("5 for Display All, 6 for Exit")
    choice=input("Enter Choice 1 to 6: ")
    if(choice=="1"): #Add Customer
        cus=Customer() #cus 1000, cus.id=0,cus.name="",cus.age=0,cus.mob=0
        cus.id=input("Enter Cust Id:")  #cus.id=10
        cus.name = input("Enter Cust Name:") #cus.name="Vikas"
        cus.age = input("Enter Cust Age:") #cus.age=39
        cus.mob = input("Enter Cust Mob:")  #cus.mob=1234
        cus.addCustomer()
        print("Customer Added Successfully")
    elif(choice=="2"):  #Search Customer
        cus=Customer()  #cus=8000, cus.id=0,cus.name="",cus.age=0..
        cus.id=input("Enter Cust Id:")  #cus.id=20
        cus.searchCustomer() #cus.id=20,cus.name=""
        showCustomer(cus)   #cus.id=20,cus.name="Anil:...




























