"""Python Continue: tkinter: GUI"""
"""
Widget: entry widget: to take the data input from user
Single line data input.
"""
# from tkinter import *
# def handler1():
#     a=v1.get()
#     print(a)
#     v1.set("")
# root=Tk()
# root.geometry("400x400")
# v1=StringVar()          #L1=[2,3,4], L1=list()
# e1=Entry(root,font=20,textvariable=v1)
# e1.grid(row=0,column=0)
# b1=Button(root,text="Submit",font=20,command=handler1)
# b1.grid(row=1,column=0)
# root.mainloop()



# #New Program
# from tkinter import *
# root=Tk()
# b1=Button(root,text="1",font=20)
# b1.grid(row=0,column=0)
# root.mainloop()

# #New Program
# from tkinter import *
# root=Tk()
# for i in range(5):
#     btn=Button(root,text=f"{i+1}",font=20,height=2,width=5)
#     btn.grid(row=0,column=i)
# root.mainloop()


# #New Program
# from tkinter import *
# root=Tk()
# count=0
# for i in range(5):
#     for j in range(5):
#         count+=1
#         btn=Button(root,text=f"{count}",font=20,height=2,width=5)
#         btn.grid(row=i,column=j)
# root.mainloop()


# #New Program
# def btn_LeftClick(e):
#     btn.config(bg="Red")
# def btn_RightClick(e):
#     btn.config(bg="Yellow")
# from tkinter import *
# root=Tk()
# root.geometry("400x400")
# btn=Button(root,text="Submit",font=20)
# btn.pack()
# btn.bind("<Button 1>",btn_LeftClick)     #to bind the events with handlers
# btn.bind("<Button 3>",btn_RightClick)     #to bind the events with handlers
# root.mainloop()


# #New Program
# def btn_LeftClick(e):   #e is the event Object
#     print(e.widget)     #e.widget is representing btn
#     print(e.widget["bg"])   #print(btn["bg"])
#     print(e.x,e.y)
#     print(e.x_root,e.y_root)
#
# from tkinter import *
# root=Tk()
# root.geometry("400x400")
# btn=Button(root,text="Submit",font=20,bg="Red")
# btn.pack()
# btn.bind("<Button 1>",btn_LeftClick)     #to bind the events with handlers
# root.mainloop()

#New Program
from tkinter import *
def handler(e):
    btn.place(x=e.x+5,y=e.y+5)
root=Tk()
root.geometry("500x500")
btn=Button(root,text="Catch Me",font=20)
btn.place(x=200,y=200)
root.bind("<Motion>",handler)

root.mainloop()
