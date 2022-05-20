"Python: GUI: Tkinter"
"""effbot.org
Pillow: PIL: Python Imaging Library
"""

"""
1. Window create:
2. At the end of program mainloop
3. Widgets and Layout/Geometry Manager
4. Widget Property
5. Name of Events
6. Bind of Events
7. Event Handlers
8. Event Attribute
"""

"""Mouse Events
Keyboard Events: 
Special Keys:<Shift>,<PgUp>,<Up>....
Character Keys: a,b,c, 1, 2, 3....
Keyboard events are generally bind with root/window 
"""
# #New Program
# from tkinter import *
# def btnLeft(e):
#     global X,Y
#     X-=5        #X=X-5
#     btn.place(x=X,y=Y)
# def btnRight(e):
#     global X,Y
#     X+=5        #X=X+5
#     btn.place(x=X,y=Y)
# root=Tk()
# root.geometry("500x500")
# X,Y=200,200
# btn=Button(root,text="Submit",font=20)
# btn.place(x=X,y=Y)
# root.bind("<Left>",btnLeft)
# root.bind("<Right>",btnRight)
# root.mainloop()


# #New Program
# from tkinter import *
# def btnLeft(e):
#     global X,Y
#     X-=5        #X=X-5
#     btn.place(x=X,y=Y)
# def btnRight(e):
#     global X,Y
#     X+=5        #X=X+5
#     btn.place(x=X,y=Y)
# def btnUp(e):
#     global X,Y
#     Y-=20
#     btn.place(x=X,y=Y)
# root=Tk()
# root.geometry("500x500")
# X,Y=200,200
# btn=Button(root,text="Submit",font=20)
# btn.place(x=X,y=Y)
# root.bind("1",btnLeft)
# root.bind("a",btnRight)
# root.bind("cetpa",btnUp)
# root.mainloop()

"https://python-course.eu/tkinter_events_binds.php"

# #New Program
# from tkinter import *
# def btnLeft(e):
#     global X,Y
#     X-=5        #X=X-5
#     btn.place(x=X,y=Y)
# def btnRight(e):
#     global X,Y
#     X+=5        #X=X+5
#     btn.place(x=X,y=Y)
# def btnUp(e):
#     global X,Y
#     Y-=20
#     btn.place(x=X,y=Y)
# root=Tk()
# root.geometry("500x500")
# X,Y=200,200
# btn=Button(root,text="Submit",font=20)
# btn.place(x=X,y=Y)
# root.bind("db",btnLeft)
# root.bind("aa",btnRight)
# root.bind("<Shift-Up>",btnUp)
# root.mainloop()


# #New Program: MoveRoot Window
# import threading
# import time
# from tkinter import *
# def moveWindow():
#     global i
#     if(i==1000):
#         i=0
#     else:
#         i+=10
#     root.geometry(f"{i}x{i}+{i}+{i}")
#     root.after(50,moveWindow)
# root=Tk()
# i=0
# # for i in range(0,1000,50):
# #     root.geometry(f"300x300+{i}+100")
#     # time.sleep(0.1)
# moveWindow()
# root.mainloop()



# #New Program
# import random
# x=random.random()
# print(x)
# y=random.randint(1,6)
# print(y)

#New Program
from tkinter import *
root=Tk()
btnNo=0
for i in range(0,3):
    for j in range(0,3):
        btnNo+=1
        btn=Button(root,text=f"{btnNo}",font=20)
        btn.grid(row=i,column=j)

randomGameButtonList=root.grid_slaves()
print(randomGameButtonList)
randomGameButtonList=root.grid_slaves(row=1)
print(randomGameButtonList)
randomGameButtonList=root.grid_slaves(row=1,column=2)
print(randomGameButtonList)
randomGameButtonList[0]["bg"]="red"



root.mainloop()