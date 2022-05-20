"""Python: tkinter"""
# from tkinter import *
# root=Tk()
# btn1=Button(root,text="ABCD",font=20)
# btn1.grid(row=0,column=0,padx=20,pady=20,ipadx=30,ipady=50)
# btn2=Button(root,text="CDEF",font=20)
# btn2.grid(row=0,column=1)
#
# root.mainloop()


# from tkinter import *
# root=Tk()
# btn1=Button(root,text="ABCD",anchor=NE,font=20,width=10,height=3)
# btn1.grid(row=0,column=0)
# btn2=Button(root,text="CDEF",font=20)
# btn2.grid(row=0,column=1,sticky=N)
#
# root.mainloop()

# #New Program
# from tkinter import *
# root=Tk()
# lbl1=Label(root,text="Enter Customer ID:",font=20,width=16,anchor=E)
# lbl1.grid(row=0,column=0)
# lbl2=Label(root,text="Enter Cust Age:",font=20,width=16,anchor=E)
# lbl2.grid(row=1,column=0)
# lbl3=Label(root,text="Enter Cust Mob:",font=20,width=16,anchor=E)
# lbl3.grid(row=2,column=0)
#
# root.mainloop()

# #New Program
# from tkinter import *
# root=Tk()
# root.geometry("500x500")
# photo=PhotoImage(file="D://cetpa/parrot1.png")
# lbl=Label(root,image=photo)
# lbl.pack()
# root.mainloop()

# #New Program
# import math
# import operator
# r1=math.pow(5,3)
# r2=operator.pow(5,3)
# print(r1,r2)

# #New Program
# from math import *      #pow=1000
# from operator import *  #pow=2000
# r1=pow(5,3)
# r2=pow(5,3)
# print(r1,r2)


# # #New Program
# # # pip install pillow: to use PIL in programs
# from tkinter import *
# from PIL import Image, ImageTk
#
# root=Tk()
# image = Image.open("D:/cetpa/parrot.jfif")
# photo1 = ImageTk.PhotoImage(image)
# label = Label(root,image=photo1)
# # label.image = photo1 # keep a reference! (Note if we directly print label.image before this line then it will show error but here we are creating a new instance variable with the object label.image to keep a reference of the image. Sometimes in functions if we create photo then as a local variable its reference goes deleted by the garbage collector once we come out of the function)
# label.pack()
# root.mainloop()

# #New Program
# import pyttsx3
# engine=pyttsx3.init()    #f=open(....)
# voices=engine.getProperty('voices')
# print(voices)
# engine.setProperty('voice',voices[1].id)
# print(type(voices[1]))
# engine.setProperty('rate', 150)
# print(type(engine))
# engine.say("Good Morning Everyone")
# engine.runAndWait()

# #New Program
# import datetime
# t=datetime.datetime.now()
# print(t)
# h=t.hour
# print(h)

# #New Program
# f=open("D://cetpa/file1.txt","r")
# print(f.read())
# f.close()

# #New Program
# with open("D://cetpa/file1.txt","r") as f:
#     print(f.read())
# print(f.read()) #Error

#New Program
import speech_recognition as sr
r=sr.Recognizer()    #recogniser class helps in recognising the audio
with sr.Microphone() as source:
     print("Listening...")
     r.pause_threshold = 0.5 #it refers to the amount of time gap after which the audio is supposed to be complete
     r.energy_threshold =300
     audio=r.listen(source) #digitaldata of whatsoever hs been spoken will be stored in audio
print("Recognising...")
query=r.recognize_google(audio,language="en-in")
print("User Said:",query)
