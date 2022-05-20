"""Backup Class"""

"""
Q. What is python?
A. Python is a programming language and any programming language is used to create softwares

Q. What are the basic requirements of a software?
A. The basic requirement is that the software:
    1. takes an input, and
    2. It provides an output
    
In python, output is provided with the help of the print() function and input is taken with the 
help of input() function

print() function:
The print function prints the values of all the arguments that have been provided to it

Syntax:
print(comma separated arguments)
"""

# x = 78
# y = 3.23
# z = "Hello"
# print(x, y, z)

"""
Q. How many arguments can be provided to the print function?
A. We can provide as many arguments as we like to the print function and they can be
of any type
Means we can provide variables, functions, methods, classes, conditions etc., can be 
provided to the print function and the print function will print all of their values
"""

# x = 78
# y = 3.23
# z = "Hello"
# print(x,y,z,56,34.78,"Welcome",type(x),x == y)


"""
Q. We have separated the arguments by commas, but how are spaces 
occuring between the values of the arguments?
Q. Why are we getting an empty line after the last argument?
Q. The values are printed horizontally, how to we print them vertically?
"""

"""
Escape Characters: These are some special characters in any programming language which when 
printed do not appear on the screen, but rather, we can see their effect.

Two most common escape characters are:

\t: This provides a tab space

\n: This takes the program into a new line
"""


# s = "Welcome to Cet\tpa. You are in py\nthon class"
# print(s)


"""
Default Arguments:
A default argument is one in which a value is provided when the function is created.
If while calling the function, we do not provide any value to it, then the function takes
the default value of that argument. But, if we provide some values to the default arguments, 
then we given priority and our values are considered

A more advanced syntax of the print function:

print(Comma Separated Arguments, sep = ' ', end = '\n')

sep: the sep argument is printed after the value of each and every argument is printed

end = after the last argument is printed, in place of sep, the end argument is printed
"""

# x = 78
# y = 3.23
# z = "Hello"
# print(x,y,z,56,34.78,"Welcome",type(x),x == y,sep = "#", end = "Hello")


"""
input function: The input() function is used to take input values from the user

Syntax to use input() function

var_name = input(string)
"""

# num1 = input("Enter first number: ")
# num2 = input("Enter second number: ")
#
# res = num1 + num2
#
# print(res)

"""
The input function takes values from the user in str format

Typecasting:
Converting one type of data into another type of data is called type casting

Syntax:

var_name = data_type(data_source)
"""
#
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
#
# res = num1 + num2
#
# print(res)

"""
Operators: These are some symbols, which perform some specific operation when they are used

Operators are of many different types:

1. Arithmetic operators
2. Conditional Operators
3. Logical Operators
4. Assignment operators
5. Membership operators
6. Identity operators
7. Bitwise operators

1. Arithmetic Operators: These are the operators which perform mathematical operations.
They are:

+   :   add
-   :   sub
*   :   multiply
/   :   divide
%   :   modulus (finds out the remainder)
//  :   floor division operator
**  :   exponent operator (finds out the power)
"""

# n1 = -12
# n2 = 5
#
# print(n1 + n2)
# print(n1 - n2)
# print(n1 * n2)
# print(n1 / n2)
# print(n1 % n2)
# print(n1 ** n2)
# print(n1 // n2)



"""
2. Conditional Operators: They check for some condition

==  :   equals to operator (2 values are equal or not)
!=  :   not equals to
>
<
>=
<=
"""

# a = 5
# b = 2
# c = 7
#
# print(a == b)
# print(a != b)
# print(c > a)
# print(c < a)
# print(b <= c)
# print(a >= b)

"""
3. Logical Operators: logical operators can check two or mode conditions at the same time

and :   It checks two conditions and returns True only when both of them are True
or  :   It checks two conditions and returns True when at least one if True
not :   It reverses the condition that it gets
"""

# a = 5
# b = 2
# c = 7

# print(a > b and b > c)      # True and False ==> False
# print(b < c and a >= b)     # True and True ==> True
# print(b > c and a < b)      # False and False ==> False

# print(a > b or b > c)      # True or False ==> True
# print(b < c or a >= b)     # True or True ==> True
# print(b > c or a < b)      # False or False ==> False

# print(not(a > b or b > c))      # not(True or False) ==> not(True) ==> False
# print(not(b < c or a >= b))     # not(True or True) ==> not(True) ==> False
# print(not(b > c or a < b))      # not(False or False) ==> not(False) ==> True


"""
4. Assignment Operators: The Assignment operators are used to assign value to a variable
They save the value on the right hand side in the variable on the left hand side

Note: All the arithmetic operators can be used as assignment operators

=   :   Assignment Operator
+=
-=
*=
/=
%=
//=
**=
"""

# x = 45
# y = x

# a = 12
# a+=4        # a = a + 4
# print(a)

# a = 12
# a-=4        # a = a - 4
# print(a)

# a = 12
# a*=4        # a = a * 4
# print(a)


"""
5. Membership Operators: Ye check karte hai ki ek chiz dusre ki member hai ya nahi

in
not in
"""

# s = "Welcome"
# print('e' in s)
# print('e' not in s)
#
# print('elc' in s)
# print('eco' in s)


"""
6. Identity Operators: They check if the address of two variables is the same or not

is
is not
"""

a = 5
b = 16
c = a

print(id(a))
print(id(b))
print(id(c))

print(a is b)
print(c is a)





