"Python"
"""
Floyd's Triangle
1
01
101
0101
10101
"""
# n=int(input("Enter No. of Lines:")) #n=5
# for i in range(n):  #i=0,1,2,3,4
#     if(i%2==0):
#         flag=1
#     else:
#         flag=0
#     for j in range(i+1):
#         print(flag,end="")
#         if(flag==1):
#             flag=0
#         else:
#             flag=1
#     print()


"""Dictionary
Dictionary is an unordered collection of key value pairs
"""
# d={2:22,3:33,4:44}
# print(d[3])
# d[4]=55
# print(d)

# #New Program
# d={2:22,3:33,4:44}
# d.pop(3)
# print(d)

# #New Program
# d={2:22,3:33,4:44}
# d.popitem()
# print(d)

# #New Program
# d={2:22,3:33,4:44}
# d1=d.copy()
# print(id(d1))
# print(id(d))

# #New Program
# d={2:22,3:33,4:44}
# d.clear()
# print(d)

# #New Program
# d={2:22,3:33,4:44}
# k=d.keys()
# print(k)

# #New Program
# d={2:22,3:33,4:44}
# k=d.values()
# print(k)

# #New Program
# d={2:22,3:33,4:44}
# k=d.items()
# print(k)

# #New Program
# d={2:22,3:33,4:44}
# k=d.get(3)
# print(k)
# print(d[3])

# #New Program
# d={2:22,3:33,4:44}
# d.update({3:59})
# print(d)
# d={2:22,3:33,4:44}
# d.setdefault(3,59)
# print(d)
# d={2:22,3:33,4:44}
# d.update({5:59})
# print(d)
# d={2:22,3:33,4:44}
# d.setdefault(5,59)
# print(d)

#New Program
# d={2:22,3:33,4:44,5:55}
# for e in d:
#     print(e)

# d={2:22,3:33,4:44,5:55}
# for e in d.values():
#     print(e)

# #New Program
# d={2:22,3:33,4:44,5:55}
# print(d.items())


# #New Program
# d={2:22,3:33,4:44,5:55}
# print(d.items())
# for k,v in d.items():
#     print(k,v)


# #New Program
# d={2:22,3:33,4:44,5:55}
# d.update({3:88,6:66})
# print(d)

# #New Program
# L1=[2,3,4,5]
# L1[5]=66
# print(L1)


# #New Program
# d={2:22,3:33,4:44,5:55}
# d[6]=66
# print(d)


"""String"""
# s="CETPA InfoTech**Pvt.**Ltd."
# r=s.lower()
# print(r) 

# #New Program
# s="CETPA InfoTech**Pvt.**Ltd."
# r=s.upper()
# print(r)

# #New Program
# s="CETPA infoTech**pvt.**Ltd."
# r=s.title()
# print(r)

# #New Program
# s="CETPA infoTech**pvt.**Ltd."
# r=s.count("info")
# print(r)

# # New Program
# s="CETPA infoTech**pvt.**Ltd."
# r=s.index("T") #Index of First Matching Element
# print(r)

# # New Program
# s="CETPA infoTech**pvt.**Ltd."
# r=s.index("info") #Index of First Matching Element
# print(r)

# # New Program
# s="abc*def*ghi"
# r=s.split("*")
# print(r)

# # New Program
# s="Vikas Kumar Kalra"
# r=s.split()
# print(r)

# #New Program
# s=input("Enter 5 Nos:")
# r=s.split()
# print(r)

# #New Program
# s=input("Enter 5 Nos:").split()
# print(s)

# #New Program
# s="CETPA InfoTech PVT. LTD."
# i=s.index("T",3)
# print(i)


"""Take 5 nos as input from user in one go and
add them '23*' """

# s=input("Enter 5 Nos:").split()
# print(s)
# r=0
# for e in s:
#     t=int(e)
#     r=r+t
# print(r)

# #New Program
# s="23.5"
# r=int(s)
# print(r)

# #New Program
# s="2345"
# f=s.isdecimal()
# print(f)
# s="23 45"
# f=s.isdecimal()
# print(f)

#New Program
# age=int(input("Enter Your Age:"))
# print(age)

# #New Program
# while(1):
#     age=input("Enter Your Age:")
#     if(age.isdecimal()):
#         if(int(age)>=1 and int(age)<=100):
#             print("Age is in Correct Format")
#             break
#         else:
#             print("Enter Age in Valid Range Only")
#     else:
#         print("Enter Age in Numbers Only")
# while(1):
#     mob=input("Enter Mob No:")


# #New Program
# s="CETPA"
# print(s.isnumeric())

# #New Program
# s=" CETPA Info"
# print(len(s))
# r=s.strip()   #Strip white spaces from starting and end
# print(len(r))

# #New Program
# s=input("Enter Your Name").strip()
# print(s)

# #New Program
# s="CETPA"
# r=s.replace("TP","1234")
# print(r)

# #New Program
# s="CETPA Infotech Pvt Ltd"
# r=s.replace(" ","**")
# print(r)
# print(s)

# #New Program
# s="CETPA"
# s[4]="$" #Error

# #New Program
# s="CETPA"
# r=s[:4]+"$"
# print(r)

# #New Program
# s="CETPA Info"
# r=s.isalpha()
# print(r)

# #New Program
# s="CETPA123"
# r=s.isalnum()
# print(r)

# #New Program
# L1=["abc","mno","aae"]
# L1.sort()
# print(L1)

# #New Program
# L1=["abc","mno",45]
# L1.sort() #Error
# print(L1)

# #New Program
# s="CETPA*Info*tech"
# print(s)
# L1=s.split("*")
# print(L1)
# r="*".join(L1)
# print(r)


















