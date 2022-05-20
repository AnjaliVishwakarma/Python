"Python Continue"
"""Once again Good Morning Everyone
Perfect Practise makes a person perfect
"""

"""
Loops: 
Hurdles:
First Level: Where we need to work on elements on 
an iterator or to create elements of a series
Second Level: To find a consolidated result through
elements of an iterator or a series.
like calculate the result of a series:
eg: To find the sum of 1 to 10
To find sum of series like 2sq+3sq+4sq+...10sq
"""


"""
Print table of 2
ie first hurdle: Access/print elements of a series
2, 4, 6, 8....20
Step 1: No of elements to print/calculate: 10
Step 2: Run the loop for that no of time
for i in range(10):
Step 3: Create a table showing relation between index and elements
i       element
0       2
1       4
2       6
.
9       20
Step 4: Through table, Find the relationship between element
and index
e=i*2+2
Step 5: print the element 
"""
# for i in range(10): #i=0,1,2,..9
#     e=i*2+2
#     print(e)

# #New Program
# for i in range(1,11): #i=1,2,10
#     e=i*2
#     print(e)        #print(i*2)
#

# #New Program
# for i in range(2,21,2):
#     print(i)


"""
Print the square of elements of a list
L1=[2,3,4,5,8,9]
"""
# L1=[2,3,4,5,8,9]
# for e in L1:
#     ele=e*e
#     print(ele)

# #New Program
# L1=[2,3,4,5,8,9]
# for i in range(len(L1)):    #i=0,1,2....5
#     ele=L1[i]*L1[i]
#     print(ele)

"""
Print the sum of table of 2
ie Second hurdle: Access elements and find the results
2+4+6+8+10+...20
Step 1: No of elements to print/calculate: 10
Step 2: Run the loop for that no of times ie 10 times
for i in range(10):
Step 3: Create a table showing relation between index and elements
i       element
0       2
1       4
2       6
.
9       20
Step 4: Through table, try to Find the relationship between element
and index
term=i*2+2  or term=(i+1)*2
Step 5: Put a formula ie result = result operator term
res=res + term
Step 6: Before starting of the loop, initialize the result
in such a way that the first time loop runs, result should
have the first term in it
res
Step 7: print the result outside the loop
"""
# x=5
# y=y+x
# print(y)
# res=res+term
#New Program: Sum of table of 2: 2+4+6+8+....20
# r=0
# for i in range(1,11):   #i=1,2,...10
#     t=i*2           #t=2,4,6
#     r=r+t           #r=2, r=2+4, r=2+4+6...+20
# print(r)

# #Sum of elements of a List:
# L1=[2,3,4,5,7,9]
# print(sum(L1))

# #Sum of elements of a List:
# L1=[2,3,4,5,7,9]  #2+3+..9
# r=0
# for e in L1:
##    t=e
#     r=r + e                #r=2+3+4...r=r+t
# print(r)

# #Sum of square of elements of a List:
# L1=[2,3,4,5,7,9]    #Res=2sq+3sq+4sq+....9sq
# r=0
# for e in L1:
#     t=e**2
#     r=r + t                #r=2sq
# print(r)

#New Program
"""
Table
i       term
8       L1[7]
7       L1[6]

1       L1[0]

"""

# #New Program
# L1=[2,3,4,5,6,7,8,9]    #0 to 7
# for i in range(len(L1),0,-1): #i=8,7,6,5...1
#     print(L1[i-1])

# #New Program
# L1=[2,3,4,5,6,7,8,9]    #0 to 7
# for i in range(len(L1),0,-1): #i=8,7,6,5...1
#     print(L1[i-1])
"""
i        Term
-1        L1[-1]
-2        L1[-2]
        .
-len(L1)        L1[-8]
"""
# L1 = [2, 3, 4, 5, 6, 7, 8, 9]  # 0 to 7, -8 to -1
# for i in range(-1,-len(L1)-1,-1):   #-1 to -8, -1 to -9
#     print(L1[i])

"""
ASCII Code/Unicodes
Capital to Small: 32 add in unicodes
Small to Capital: -32
A: 65           a: 97   
B: 66           b: 98
C: 67           c: 99

.
Z: 90           z: 122

ord(ch): Return ASCII/Unicode
chr(unicode): Return Character
Name: Capital to Small letter
"""
# print(ord("A"))
# print(chr(65))


"""
Third Level: Nested Loops
Loops inside loops
"""

# L1=[[2,3,4],[5,6,7]]    #2*3
# for e in L1:            #2  e=[2,3,4]
#     for a in e:         #3
#         print(a)        #6 times execute


# #New Program
# a,b,c=[2,3,4]   #Direct Unpacking
# print(a,b,c)

# #New Program
# a,b,c,d=[2,3,4]   #Error
# print(a,b,c)

# #New Program
# a,b=[2,3,4]   #Error
# print(a,b)



# #New Program
# L1=[[2,3,4],[5,6,7]]
# for a,b,c in L1:    #Unpacking Concept
#     print(a,b,c)

# #New Program: i*j*k...
# for i in range(3):  #3 times, i=0,1,2
#     for j in range(2):  #2 times, j=0,1
#         print("CETPA")  #6 times

"""

"""

