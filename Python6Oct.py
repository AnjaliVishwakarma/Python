"Doubts of Last Day Session"
# #New Program: i*j*k...
# for i in range(3):  #3 times, i=0,1,2
#     for j in range(2):  #2 times, j=0,1
#         print("CETPA")  #6 times. n*m times

# #New Program
# for i in range(3):  #3 times, i=0,1,2
#     print("CETPA")
#     print("Hello")
# print("Complete")

# #New Program
# for i in range(3):  #3 times, i=0,1,2
#     for j in range(2):
#         print("CETPA")
#         print("Hello")
#     print("Partially Complete")
# print("Complete")

# #New Program
# m,n=3,4
# for i in range(m):
#     for j in range(n):
#         print("CETPA")  #m*n times

# # #New Program
# for i in range(3):
#     for j in range(2):
#         print("CETPA")

"""
Debugging: Firstly put a break point by mouse click
on the left pane and then right click and run the 
program in debug mode and then click on F7 or F8 as
required. 
"""

# #New Program: Debug Mode
# #BLL
# def add(a,b):
#     r=a+b
#     return r
# #BL
# u,v=5,7
# s=add(u,v)
# print(s)

"""Perfect Practise Makes a Person Perfect"""

"""
Loops inside loop: Nested loops
Pattern Printing
"""

"""
*
**
***
****
*****
i       n
0       1
1       2
2       3
3       4
4       5
n=i+1
"""
# m=int(input("Enter Any No:"))   #m=5
# for i in range(m):  #i=0,1,2,3,4
#     n=i+1
#     for j in range(n):  #n=1, n=2   #for j in range(i+1)
#         print("*",end="")
#     print()

"""
*****
****
***
**
*
i       j_max
0       n
1       n-1
2       n-2
3       n-3
4       n-4

"""
# n=int(input("Enter Any No:"))   #n=5
# for i in range(n):  #i=0,1,2,3,4
#     for j in range(n-i):
#         print("*",end="")
#     print()


"""
    *
   **
  ***
 ****
*****
i       j_max   k_max
0       n-1     1
1       n-2     2
2       n-3     3
"""
# #New Program
# n=int(input("Enter Any No:"))
# for i in range(n):  #i=0,1,2,3,4
#     for j in range(n-i-1):
#         print(" ",end="")
#     for k in range(i+1):
#         print("*",end="")
#     print()

"""
*        *
**      **
***    ***
****  ****
**********
i   j_max   k_max
0   1       8 ie 2n-2    
1   2       6 ie 2n-4
2   3       4 ie 2n-6
3   4
4   5
k_max=2n-2i-2
"""
# n=int(input("Enter No. of Lines:")) #n=5
# for i in range(n):          #i=0,1,2,3,4
#     for j in range(i+1):
#         print("*",end="")
#     for k in range(2*n-2*i-2):  #for j in range(2*(n-i-1)):
#         print(" ",end="")
#     for l in range(i+1):
#         print("*",end="")
#     print()

"""
1
22
333
4444
55555
"""

"""
break and continue keyword

break: to stop the program at some particular iteration
continue: to skip the particular iteration or part of the
iteration.
"""

# #New Program 1sq,2sq,3sq,4sq
# for i in range(1,10):
#     if(i==5):
#         break
#     print(i**2)

# #New Program 1sq,2sq,3sq,4sq
# for i in range(1,10):
#     print(i**2)
#     if (i == 4):
#         break

# #New Program: 1sq,2sq,3sq,4sq,6sq,7sq,9sq,10sq
# for i in range(1,11):
#     if(i==5 or i==8):
#         continue
#     print(i**2)

#Thankyou very much

"""
SQL: Lang


MySQL: Database Server
Oracle:
MS Access:
MS SQL Server


DS: Python, DA, ML, SQL, Tableau, Advance Excel, SAS,
Power BI..........
"""



