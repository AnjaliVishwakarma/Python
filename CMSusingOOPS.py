"""Python OOPS"""
"""CMS: Customer Management System
Add Customer, Search Customer, Delete Customer, Modify Customer
"""
#BLL
class Customer:
    cuslist=[]  #Customer.cuslist=[1000,2000,3000...
    def __init__(self):
        self.id=0
        self.name=""
        self.age=0
        self.mob=0
    def addCustomer(self):  #self.id=10,self.name="Vikas"...
        Customer.cuslist.append(self)
    def searchCustomer(self): #self=8000, self.id=20
        for e in Customer.cuslist:
            if(e.id==self.id):
                self.name=e.name
                self.age=e.age
                self.mob=e.mob
    @staticmethod
    def deleteCustomer(id):     #id=20
        for e in Customer.cuslist:
            if(e.id==id):
                Customer.cuslist.remove(e)
                return
    def modifyCustomer(self):#self=9000,self.id=30,self.name="Sonu"...
        for e in Customer.cuslist:
            if(e.id==self.id):
                e.name=self.name
                e.age=self.age
                e.mob=self.mob
                return







#PL
def showCustomer(cus):
    print("Cust Id:",cus.id,"Cust Name:",cus.name,"Cust Age:",cus.age,"Cust Mob:",cus.mob)
while(1):
    print("1 for Add Cust, 2 for Search Cust")
    print("3 for Delete Cust, 4 for Modify Cust")
    print("5 for Display All, 6 for Exit")
    choice=input("Enter Choice 1 to 6: ")
    if(choice=="1"): #Add Customer
        cus=Customer() #cus 1000, cus.id=0,cus.name="",cus.age=0,cus.mob=0
        cus.id=input("Enter Cust Id:")  #cus.id=10
        cus.name = input("Enter Cust Name:") #cus.name="Vikas"
        cus.age = input("Enter Cust Age:") #cus.age=39
        cus.mob = input("Enter Cust Mob:")  #cus.mob=1234
        cus.addCustomer()
        print("Customer Added Successfully")
    elif(choice=="2"):  #Search Customer
        cus=Customer()  #cus=8000, cus.id=0,cus.name="",cus.age=0..
        cus.id=input("Enter Cust Id:")  #cus.id=20
        cus.searchCustomer() #cus.id=20,cus.name=""
        showCustomer(cus)   #cus.id=20,cus.name="Anil:...
    elif(choice=="3"):  #Delete Customer
        id=input("Enter Cust Id:")
        Customer.deleteCustomer(id)     #id=20
        print("Customer Deleted Successfully")
    elif(choice=="4"): #Modify Customer
        cus=Customer()  #cus=9000,cus.id=0,cus.name=0....
        cus.id=input("Enter Customer Id:")  #cus.id=30
        cus.name=input("Enter Cust Updated Name:") #Sonu
        cus.age = input("Enter Cust Updated Age:")  #55
        cus.mob = input("Enter Cust Updated Mob:")  #5555
        cus.modifyCustomer()
        print("Customer Modified Successfully")
    elif(choice=="5"): #Display All Customers
        for e in Customer.cuslist:
            showCustomer(e)
    elif(choice=="6"): #Exit
        break
    else:
        print("Incorrect Choice, Try Again")




















