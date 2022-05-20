"""Python"""
"""Exception Handling in Python
Exceptions: Errors or Run Time Errors
"""
# a=int(input("Enter First No:"))
# b=int(input("Enter Second No:"))
# s=a+b
# print(s)

# #New Program
# a=int(input("Enter First No:"))
# b=int(input("Enter Second No:"))
# s=a+b
# print(s)

# #New Program
# x="cetpa"
# print(x[7])

# #New Program
# while(1):
#     a=input("Enter First No:")
#     if(a.isdecimal()):
#         a=int(a)
#         break
#     else:
#         print("Incorrect Input")
# while(1):
#     b=input("Enter Second No:")
#     if(b.isdecimal()):
#         b=int(b)
#         break
#     else:
#         print("Incorrect Input")
# s=a+b
# print(s)

"""In Python for handling exceptions, we have 4 keywords
1. try
2. except
3. finally
4. raise

In Python we have many predefined exception classes to 
represent different kind of errors.
And Exception class is the parent to all exception classes.
"""
# try:
#     a=int(input("Enter First No:"))
#     b=int(input("Enter Second No:"))
#     s=a+b
#     print(s)
# except:
#     print("Incorrect Input")

# New Program
# while(1):
#     try:
#         a=int(input("Enter First No:"))
#         b=int(input("Enter Second No:"))
#         s=a+b
#         print(s)
#         break
#     except:
#         print("Incorrect Input")

# #New Program
# a=int(input("Enter First No:"))
# b=int(input("Enter Second No:"))
# s=a/b
# print(s)


# #New Program: Divison of two numbers
# while(1):
#     try:
#         a=int(input("Enter First No:"))
#         b=int(input("Enter Second No:"))
#         s=a/b
#         print(s)
#         break
#     except:
#         print("Incorrect Input")


# #New Program: Division of Two Numbers
# while(1):
#     try:
#         a=int(input("Enter First No:"))
#         b=int(input("Enter Second No:"))
#         r=a/b
#         print("Result:",r)
#         break
#     except ValueError:
#         print("Enter the Inputs as Whole Numbers Only")
#     except ZeroDivisionError:
#         print("Enter Non Zero Second Input")
#     except Exception:
#         print("There is some error, try again")

# #New Program: Division of Two Numbers
# while(1):
#     try:
#         a=int(input("Enter First No:"))
#         b=int(input("Enter Second No:"))
#         r=a/b
#         print("Result:",r)
#         break
#     except Exception:
#         print("There is some error, try again")

# #New Program
# a=int(input("Enter First No:"))
# b=int(input("Enter Second No:"))
# r=a/b
# print("Result:",r)


# #New Program: Division of Two Numbers
# while(1):
#     try:
#         a=int(input("Enter First No:"))
#         b=int(input("Enter Second No:"))
#         r=a/b
#         print("Result:",r)
#         break
#     except Exception as e:    #e is user defined
#         print("Error!",e)
#         print(type(e))

# #New Program: Division of Two Numbers
# while(1):
#     try:
#         a=int(input("Enter First No:"))
#         b=int(input("Enter Second No:"))
#         r=a/b
#         print("Result:",r)
#         break
#     except ValueError:
#         print("Error! Enter Whole Number Inputs Only")
#     except ZeroDivisionError:
#         print("Error! Enter Non Zero Second Input")
#     except Exception as e:    #e is user defined
#         print("Error!",e)


"""
finally: is the keyword which executes always even if
there is error in the program or there is no error in the
program
"""
# #Calci
# while(1):
#     try:
#         no1=int(input("Enter First No:"))
#         no2 = int(input("Enter Second No:"))
#         choice=input("Enter Choice +, -, *, / :")
#         if(choice=="+"):
#             r=no1+no2
#             print("Result:",r)
#         elif (choice == "-"):
#             r = no1 - no2
#             print("Result:", r)
#         elif (choice == "*"):
#             r = no1 * no2
#             print("Result:", r)
#         elif (choice == "/"):
#             r = no1 / no2
#             print("Result:", r)
#         else:
#             print("Incorrect Choice")
#     except ValueError:
#         print("Error: Enter Whole Numbers Only")
#     except ZeroDivisionError:
#         print("Error: Enter Non Zero Second Input")
#     except Exception as err:
#         print("Error:",err)
#     finally:
#         ch=input("Wanna Continue Y/N?")
#         if(ch=="N" or ch=="n"):
#             break

"3 Minutes Break: 5: 40 PM"

#New Program: Enter few input numbers in one go and
#convert them to int
# L1=input("Enter Few Numbers:").split()
# print(L1)
# for i in range(len(L1)):
#     L1[i]=int(L1[i])
# print(L1)



"""raise keyword: 
# 70% Communication Skills
# 30% Technical Skills
# 
# 70% Communication Skills
# 30% Technical Skills

raise is the keyword through which we raise the 
exceptions in the program


Core Python  + Intermediate Python: 70%
"""

#Calci
while(1):
    try:
        no1=int(input("Enter First No:"))
        no2 = int(input("Enter Second No:"))
        choice=input("Enter Choice +, -, *, / :")
        if(choice=="+"):
            r=no1+no2
            print("Result:",r)
        elif (choice == "-"):
            r = no1 - no2
            print("Result:", r)
        elif (choice == "*"):
            r = no1 * no2
            print("Result:", r)
        elif (choice == "/"):
            r = no1 / no2
            print("Result:", r)
        else:
            raise NotImplementedError("Incorrect Choice")
    except ValueError:
        print("Error: Enter Whole Numbers Only")
    except ZeroDivisionError:
        print("Error: Enter Non Zero Second Input")
    except NotImplementedError as err:
        print("Error!",err)
    except Exception as err:
        print("Error:",err)
    finally:
        ch=input("Wanna Continue Y/N?")
        if(ch=="N" or ch=="n"):
            break












