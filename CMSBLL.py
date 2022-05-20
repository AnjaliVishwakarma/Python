#BLL
import pickle
import json
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
                return 1
        raise NotImplementedError("Id not Found")


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
    @staticmethod
    def savetoPickle():
        f=open("D://cetpa/filepickle.txt","wb")
        pickle.dump(Customer.cuslist,f)
        print("Data Saved Successfully in Pickle Format")
        f.close()

    @staticmethod
    def loadfromPickle():
        f = open("D://cetpa/filepickle.txt", "rb")
        Customer.cuslist=pickle.load(f)
        print("Data Retrieved Successfully")
        f.close()
    @staticmethod
    def sortCriteria(ob):
        return ob.id
    @staticmethod
    def sortbyId():
        Customer.cuslist.sort(key=Customer.sortCriteria)
    @staticmethod
    def convtoDict(obj):
        return obj.__dict__
    @staticmethod
    def savetoJson():
        f=open("D:/cetpa/filejson.txt","w")
        json.dump(Customer.cuslist,f,default=Customer.convtoDict)
        f.close()
    @staticmethod
    def convtoObj(d):   #d={"id":"10","name":"vikas","age":"39","mob":1234}
        cus=Customer()
        cus.id=d["id"]
        cus.name = d["name"]
        cus.age = d["age"]
        cus.mob = d["mob"]
        return cus
    @staticmethod
    def loadfromJson():
        f = open("D:/cetpa/filejson.txt", "r")
        Customer.cuslist=json.load(f, object_hook=Customer.convtoObj)
        f.close()