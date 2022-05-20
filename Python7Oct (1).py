"""Python"""
"""
*     *
*     *
*     *
*******
*     *
*     *
*     *

"""


"""
    *
   * *
  * * *
 * * * *
* * * * *
"""
# n=7
# for i in range(n):  #i=0
#     for j in range(n-i-1):
#         print(" ",end="")
#     for k in range(i+1):
#         print("* ",end="")
#     print()

#New Program:
"""Prime No: Only divisible by 1 and itself: 7"""
# n=int(input("Enter Any No:"))
# flag=0
# for i in range(2,n):    #i=2,3,4,5,6
#     if(n%i==0):
#         print("The Entered No is not Prime")
#         flag=1
#         break
# if(flag==0):
#     print("The Entered No is Prime")

"""else with loops executes only when loop completes
normally after all iterations, in case break keyword
executes inside loop then else condition of loop
wont execute"""
# #New Program
# n=int(input("Enter Any No:"))
# for i in range(2,n):    #i=2,3,4,5,6
#     if(n%i==0):
#         print("The Entered No is not Prime")
#         break
# else:
#     print("The Entered No is Prime")


# """Find all prime and non prime nos in a given range"""
# n1=int(input("Enter Lower No:"))     #n1=5
# n2=int(input("Enter Lower No:"))     #n2=15
# for n in range(n1,n2+1):    #n=5,6,7,....15
#     for i in range(2,n):    #i=2,3,4,5,6
#         if(n%i==0):
#             print(n," is not Prime")
#             break
#     else:
#         print(n," is Prime")

"""
While Loop

for i in range(a,n,s):
    set of statements

i=a     #Initialize with lower bound
while(i<n):  #check i is less than upper bound
    set of statements
    i+=s        #Increment i by step size

"""
# for i in range(5):
#     print("CETPA")

# #New Program
# i=0
# while(i<5):
#     print("CETPA")
#     i+=1

"""Find all prime and non prime nos in a given range
using while loop"""
# n1=int(input("Enter Lower No:"))     #n1=5
# n2=int(input("Enter Lower No:"))     #n2=15
# n=n1
# while(n<n2+1):  #while(n<=n2)
# # for n in range(n1,n2+1):    #n=5,6,7,....15
#     i=2
#     while(i<n):
# #     for i in range(2,n):    #i=2,3,4,5,6
#         if(n%i==0):
#             print(n," is not Prime")
#             break
#         i+=1
#     else:
#         print(n," is Prime")
#     n+=1

"""While loop as an infinite loop
while(if True) then always run

while (True)    : Always run
while (Any Non Zero or Non None Value)  #Always run

Won't run for a single time
while(False)
while(0)
while(None)
"""
#Infinite While loop
# while(1):print("CETPA")

# while(-777.89):
#     print("CETPA")

# while(0):
#     print("CETPA")

#New Program
# for i in range(50,20):
#     print("CETPA")

s=(2+3)*4

"""Tuple"""
# t=(5,)
# print(type(t))
# t=(5,6)
# print(type(t))

# #New Program
# t=tuple()
# print(t)
# print(type(t))

# #New Program
# L1=list()   #Object of List Class
# print(L1)

# #New Program
# t=(22,33.4,(3,4,5),[5,6])
# print(t)
# print(type(t))

# #New Program
# t=(22,33,44,55,33)
# i=t.index(44)
# print(i)
# n=t.count(33)
# print(n)

"""Loops complete
Tuple Complete"""

"""Break: 2 Min: 5:22PM"""

"""A fresh batch is going to start from coming Monday
on Data Analytics

DA vs DS:

DA Life Cycle:
Collect the Data from different sources
Data Pre processing: common format, common units
Data Clean: Garbage value, outliers 
Data Analyse
Data Visualize
Statistics
DA: To find important insights from the Data

DS:  To make some future predictions or forecasting

DS=DA+ML

ML: Algo


Full Stack: End to End Developer
Python + Django: Web Development: Full Stack Development
HTML, CSS, JS, JQuery, Bootstrap: Web Designing
MySQL: Database

Angular,
React

Next Topic: Dictionary 

Dictionary: Collection of Key, Value Pairs
d={key1:value1,key2:value2......}
Dictionary is Mutable in nature
Collection of heterogeneous data type
Dictionary keys must be unique
Hashing: Self Study
"""
# d={22:"CETPA",11:99,"abc":23.5,85:[22,33,44]}
# print(d)
# print(type(d))
# print(d[11])
# print(d["abc"])

# #New Program
# d={1:11,2:22,3:33,2:88,5:11}
# print(d)
# print(len(d))

# New Program
# L1=[22,33,44,55....]











