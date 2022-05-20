"""Python GUI Programming"""

"""GUI Programming: Graphical User Interface
GUI: 
    Desktop Application: tkinter
    Web Applications: django
    Mobile Applications: kivy
"""

"""Desktop Application: tkinter
tkinter: Tool Kit Interface
tkinter is designed on top of TCL/TK

"""

# import tkinter as tk
# root=tk.Tk()  #root object of Tk()
#
# root.mainloop() #Infinte Loop
# print("CETPA")

# #New Program
# from tkinter import *
# root=Tk()  #root object of Tk()
#
# root.mainloop() #Infinte Loop

# #New Program
# import tkinter
# root=tkinter.Tk()  #root object of Tk()
# root.geometry("300x500")
# root.mainloop() #Infinte Loop to hold the root window


# #New Program
# import tkinter
# root=tkinter.Tk()  #root object of Tk()
# root.geometry("300x500+200+200")
# root.mainloop() #Infinte Loop to hold the root window

# #New Program
# from tkinter import *
# root=Tk()
# root.geometry("200x300+100+250")
# root.mainloop()

"""On Root window, we have to create different kind
of widgets. Ex: Button, Menu, RadioButton, Entry, Text....

In Python, we have different classes for different 
widgets and to create widget on any window, we need
to create object of that class.

"""

"""
In tkinter we have 3 types of geometries ie the location
to place widget on window
1. pack geometry:
widget.pack(side="left") By default side is 'top'
top, left, right, bottom
2. place geometry: pixels
widget.place(x=100,y=100)
3. grid geometry: rows and column
widget.grid(row=row_no,column=column_no)

It is highly recommended to use one type of 
geometry on one window

"""
# #New Program
# import tkinter as tk
# root=tk.Tk()
# root.geometry("400x300")
# btn=tk.Button(root,text="Submit")
# btn.pack(side="right")
# root.mainloop()


# #New Program
# import tkinter as tk
# root=tk.Tk()
# root.geometry("400x300")
# btn1=tk.Button(root,text="Submit")
# btn1.pack(side="right")
# btn2=tk.Button(root,text="CETPA")
# btn2.pack()
# root.mainloop()

# #New Program
# from tkinter import *
# root=Tk()
# root.geometry("300x300")
# btn=Button(root,text="Submit",bg="Red",fg="Yellow",font=10)
# btn.pack(side="bottom")
# root.mainloop()


# #New Program
# from tkinter import *
# root=Tk()
# root.geometry("300x300")
# btn1=Button(root,text="Submit",bg="#7395D3",fg="Yellow",font=10)
# btn1.place(x=50,y=150)
# btn2=Button(root,text="Submit",bg="orange",fg="Yellow",font=10)
# btn2.place(x=100,y=200)
# root.mainloop()

# #New Program
# from tkinter import *
# root=Tk()
# root.geometry("300x300")
# btn1=Button(root,text="Submit",bg="#7395D3",fg="Yellow",font=10)
# btn1.grid(row=0,column=0)
# btn2=Button(root,text="Submit",bg="orange",fg="Yellow",font=10)
# btn2.grid(row=5,column=0)
# root.mainloop()

# #New Program
# from tkinter import *
# root=Tk()
# root.geometry("300x300")
# btn1=Button(root,text="Submit",width=10,height=3,bg="#7395D3",fg="Yellow",font=10)
# btn1.grid(row=0,column=0)
# btn2=Button(root,text="Submit",bg="orange",fg="Yellow",font=("Impact",50))
# btn2.grid(row=5,column=0)
# root.mainloop()


"""
Event Based Programming

Event: Any Action.

We need to consider only important events.
Device Inputs: Events pass.

Mouse Events like:
left click, right click, left click release...
left double click..
mouse motion with mouse left click hold
mouse motion without button click
..

Keyborad Events:
All button clicks 
sequence of button clicks

Event Handlers are the program codes (functions) which 
executes once an event is fired.
Event Handler/Call back/Listner/sub routine: function

"""


# from tkinter import *
# def btn_Click():
#     print("I am Clicked")
# root=Tk()
# root.geometry("300x300")
# btn=Button(root,text="Submit",font=20,command=btn_Click)
# btn.pack()
# root.mainloop()

# #New Program
# from tkinter import *
#
# root=Tk()
# root.geometry("300x300")
# root.title("My First GUI")
# root.state("zoomed")
# root.mainloop()


"""
To pass the properties to a widget, we have multiple
options as follows:
1. widget=Widget_Class_Name(Properties)
2. widget["property_name"]="property_value"
3. widget.config(property_name="property_value")
"""
# from tkinter import *
# root=Tk()
# root.geometry("300x300")
# btn=Button(root,bg="Yellow",font=1)
# btn["text"]="Submit"
# btn["fg"]="blue"
# btn.config(width=15,height=4)
# btn.grid(row=0,column=0)
# root.mainloop()


# from tkinter import *
# def func1():
#     print("CETPA")
# root=Tk()
# root.geometry("300x300")
# btn=Button(root,bg="Yellow",font=1,command=func1)
# btn["text"]="Submit"
# btn["fg"]="blue"
# btn.config(width=15,height=4)
# btn.grid(row=0,column=0)
# root.mainloop()

# #New Program
# from tkinter import *
# root=Tk()
# root.geometry("500x500")
# lbl=Label(root,text="Enter Your Name:",font=("Arial",20),fg="Orange")
# lbl.grid(row=0,column=0)
# root.mainloop()

# #New Program
# from tkinter import *
# root1=Tk()
# root1.geometry("200x200+100+100")
# root2=Tk()
# root2.geometry("200x200+200+200")
# root3=Tk()
# root3.geometry("200x200+300+300")
# root1.mainloop()

"Entry Widget: To get the data input from keyboard in" \
"single line"
# #New Program
# from tkinter import *
# def btn_Click():
#     name=var.get()
#     print(name)
# root=Tk()
# root.geometry("500x500")
# lbl=Label(root,text="Enter Your Name:",font=20)
# lbl.grid(row=0,column=0)
# var=StringVar()
# entr=Entry(root,font=20,textvariable=var)
# entr.grid(row=0,column=1)
# btn=Button(root,text="Submit",font=20,command=btn_Click)
# btn.grid(row=1,column=1)
#
# root.mainloop()


# #New Program
# from tkinter import *
# def btn_Click():
#     root1=Tk()
# root=Tk()
# root.geometry("500x500")
# btn=Button(root,text="Submit",font=20,command=btn_Click)
# btn.grid(row=1,column=1)
#
# root.mainloop()








