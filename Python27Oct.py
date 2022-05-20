"""Python: JSON Continue"""
# class C1:
#     def __init__(self):
#         self.a=5
#         self.b=10
# ob=C1()
# print(ob.__dict__)

#New Program
"""
Delegation Model or 
Function Pointer: Function Pointer is a variable which
holds the address of a function. 
The process of holding the address of a function in a 
variable is called Delegation Model.
"""
# def add(a,b):
#     return a+b
#
# print(add)
# print(type(add))
# m=add   #m is a function pointer
# print(m)
# print(type(m))
# print(m(2,3))

"""In Python, we can pass even functions inside function
call"""

# #New Program
# def Prog1(m,n):
#     r=m(5)+n(4)
#     return r
# def func1(a):
#     return a**2
# def func2(a):
#     return a**3
# r=Prog1(func1,func2)    #m=func1,n=func2
# print(r)


#New Program
# L1=[23,55,67,89,32,34,56,77]
# L1.sort()
# print(L1)

# #New Program
# class Customer:
#     cuslist=[]
#     def __init__(self,id,name,age,mob):
#         self.id=id
#         self.name=name
#         self.age=age
#         self.mob=mob
# def sortCriteria(ob):
#     return ob.name
# cus=Customer(10,"vikas",39,1234)
# Customer.cuslist.append(cus)
# cus=Customer(30,"Amit",45,3456)
# Customer.cuslist.append(cus)
# cus=Customer(20,"Anil",41,2345)
# Customer.cuslist.append(cus)
# print(Customer.cuslist[1].id)
# Customer.cuslist.sort(key=sortCriteria)
# for cus in Customer.cuslist:
#     print(cus.id,cus.name,cus.age,cus.mob)


# #New Program
# def mySort(L,reverse=False):  #L= [30,25,20,45,60,55]
#     if(reverse==False):
#         for i in range(len(L)-1):       #i=0,1
#             for j in range(i+1,len(L)): #j=1,2
#                 if(L[i]>L[j]):
#                     L[i],L[j]=L[j],L[i]
#     else:
#         for i in range(len(L)-1):       #i=0,1
#             for j in range(i+1,len(L)): #j=1,2
#                 if(L[i]<L[j]):
#                     L[i],L[j]=L[j],L[i]
# L1=[30,25,20,45,60,55]
# mySort(L1,reverse=True)
# print(L1)

# #New Program#L= [30,25,20,45],
# #i=0, j=1, L=[25,30,20,45]
# #i=0, j=2, L=[20,30,25,45]
# #i=0, j=3
# def mySort(L):
#     for i in range(len(L)-1):    #i=0,1,2
#         for j in range(i+1,len(L)): #j=1,2,3
#             if(L[i]>L[j]):
#                 L[i],L[j]=L[j],L[i]
# L1=[30,25,20,45]
# mySort(L1)  #L=L1
# print(L1)


# #New Program
# def func1(a):
#     return 1/a
# m=func1
# if(m(5)>m(7)):
#     print("Welcome")
# else:
#     print("CETPA")

# #New Program
# def func1(a):
#     return 1/a
# def func2(m):
#     if(m(5)>m(7)):
#         print("Welcome")
#     else:
#         print("CETPA")
#
# func2(func1)    #m=func1

# #New Program
# class Customer:
#     cuslist=[]
#     def __init__(self,id,name,age,mob):
#         self.id=id
#         self.name=name
#         self.age=age
#         self.mob=mob
# def sortCriteria(ob):
#     return ob.id
# def mySort(L,key=None):
#     if(key!=None):
#         for i in range(len(L)-1):    #i=0,1,2
#             for j in range(i+1,len(L)): #j=1,2,3
#                 if(key(L[i])>key(L[j])):
#                     L[i],L[j]=L[j],L[i]
#     else:
#         for i in range(len(L)-1):    #i=0,1,2
#             for j in range(i+1,len(L)): #j=1,2,3
#                 if(L[i]>L[j]):
#                     L[i],L[j]=L[j],L[i]
# cus=Customer(10,"vikas",39,1234)
# Customer.cuslist.append(cus)
# cus=Customer(30,"Amit",45,3456)
# Customer.cuslist.append(cus)
# cus=Customer(20,"Anil",41,2345)
# Customer.cuslist.append(cus)
# mySort(Customer.cuslist,key=sortCriteria)  #key
# for e in Customer.cuslist:
#     print(e.id,e.name,e.age,e.mob)


# #New Program
# L1=[20,30,25]
# L1.sort()


#New Program
from tkinter import *
def func1():
    btn.config(fg="red")

root=Tk()
root.geometry("400x400")
btn=Button(root,text="Submit",font=20,command=func1)
btn.pack()

root.mainloop()




























