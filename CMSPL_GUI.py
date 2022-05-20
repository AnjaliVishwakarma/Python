from CMSBLL import *
from tkinter import *
from tkinter import messagebox
def btnAdd_Click():
    cus=Customer()
    cus.id=varId.get()
    cus.name = varName.get()
    cus.age = varAge.get()
    cus.mob = varMob.get()
    cus.addCustomer()
    messagebox.showinfo("CMS","Customer Added Successfully")
    varId.set("")
    varName.set("")
    varAge.set("")
    varMob.set("")
def btnSearch_Click():
    cus=Customer()  #
    cus.id=varId.get()
    cus.searchCustomer()
    varName.set(cus.name)
    varAge.set(cus.age)
    varMob.set(cus.mob)

def btnDelete_Click():
    pass
def btnModify_Click():
    pass
def btnShowAll_Click():
    rootCustomers=Tk()
    lblIdHead=Label(rootCustomers,text="CUST ID",font=20,width=15,bg="Red")
    lblIdHead.grid(row=0,column=0)
    lblNameHead = Label(rootCustomers, text="CUST NAME", font=20, width=15, bg="Red")
    lblNameHead.grid(row=0, column=1)
    lblAgeHead = Label(rootCustomers, text="CUST AGE", font=20, width=15, bg="Red")
    lblAgeHead.grid(row=0, column=2)
    lblMobHead = Label(rootCustomers, text="CUST Mob", font=20, width=15, bg="Red")
    lblMobHead.grid(row=0, column=3)
    row=0
    for e in Customer.cuslist:
        row+=1
        lblcusId=Label(rootCustomers,text=f"{e.id}",font=20,width=15,bg="Yellow")
        lblcusId.grid(row=row,column=0)
        lblcusName = Label(rootCustomers, text=f"{e.name}", font=20, width=15, bg="Yellow")
        lblcusName.grid(row=row, column=1)
        lblcusAge = Label(rootCustomers, text=f"{e.age}", font=20, width=15, bg="Yellow")
        lblcusAge.grid(row=row, column=2)
        lblcusMob = Label(rootCustomers, text=f"{e.mob}", font=20, width=15, bg="Yellow")
        lblcusMob.grid(row=row, column=3)

def btnExit_Click():
    root.destroy()

def btnPickleSave_Click():
    Customer.savetoPickle()
def btnPickleLoad_Click():
    Customer.loadfromPickle()


root=Tk()
root.geometry("600x500")
# root.config(bg="Orange")

lblId=Label(root,text="Enter Cust Id:",font=20)
lblId.grid(row=0,column=0)
varId=StringVar()
entrId=Entry(root,font=20,textvariable=varId)
entrId.grid(row=0,column=1)

lblName=Label(root,text="Enter Cust Name:",font=20)
lblName.grid(row=1,column=0)
varName=StringVar()
entrName=Entry(root,font=20,textvariable=varName)
entrName.grid(row=1,column=1)

lblAge=Label(root,text="Enter Cust Age:",font=20)
lblAge.grid(row=2,column=0)
varAge=StringVar()
entrAge=Entry(root,font=20,textvariable=varAge)
entrAge.grid(row=2,column=1)

lblMob=Label(root,text="Enter Cust Mob:",font=20)
lblMob.grid(row=3,column=0)
varMob=StringVar()
entrMob=Entry(root,font=20,textvariable=varMob)
entrMob.grid(row=3,column=1)

btnAdd=Button(root,text="Add Cust",width=15,height=2,font=20,command=btnAdd_Click)
btnAdd.grid(row=4,column=0)

btnSearch=Button(root,text="Search Cust",width=15,height=2,font=20,command=btnSearch_Click)
btnSearch.grid(row=4,column=1)

btnDelete=Button(root,text="Delete Cust",font=20,width=15,height=2,command=btnDelete_Click)
btnDelete.grid(row=4,column=2)

btnModify=Button(root,text="Modify Cust",width=15,height=2,font=20,command=btnModify_Click)
btnModify.grid(row=5,column=0)

btnShowAll=Button(root,text="Display All",width=15,height=2,font=20,command=btnShowAll_Click)
btnShowAll.grid(row=5,column=1)

btnExit=Button(root,text="Exit",font=20,width=15,height=2,command=btnExit_Click)
btnExit.grid(row=5,column=2)

btnPickleSave=Button(root,text="Save to Pickle",width=15,height=2,font=20,command=btnPickleSave_Click)
btnPickleSave.grid(row=6,column=0)

btnPickleLoad=Button(root,text="Load from Pickle",width=15,height=2,font=20,command=btnPickleLoad_Click)
btnPickleLoad.grid(row=6,column=1)

root.mainloop()