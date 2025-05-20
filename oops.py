'''class Student:
    name="siri"
s1=Student() 
print(s1.name)   
s2=Student()
'''

'''class car:
    color="blue"
    brand="BMW"

car1=car()
print(car1.color)
print(car1.brand)  '''


'''class Student:
    def __init__(self,name,marks):
        self.n=name 
        self.m=marks
        print("new student db")
    def hello(self):
        print("HEllo",self.n)
    def marks(self):
        print("marks of",self.n,"are",self.m)    

s1=Student("karim",45)
print(s1.n,s1.m) 
s2=Student("arjun",43)
print(s2.n,s2.m) 
s1.hello()
s2.marks()
'''

'''class Student:
    def __init__(self,name,marks):
        self.name=name 
        self.marks=marks
    def avg(self):
        sum=0
        for e in self.marks:
            sum+=e
        print("avg of",self.name,"is",sum/3)
s1=Student("karim",[43,45,47])
s2=Student("Arya",[43,43,42])
s1.avg()     
s2.avg()   
s1.name="ruci"
s1.avg()'''


class Acc:
    def __init__(self,bal,acc):
        self.bal=bal 
        self.acc=acc
    def debit(self,amnt):
        self.bal-=amnt 
        print("rs.",amnt,"was debited")
        print("toatal balance=",self.getbalnce())
    def credit(self,amnt):
        self.bal+=amnt    
        print("rs.",amnt,"was credited")
        print("toatal balance=",self.getbalnce())
    def getbalnce(self):
        return self.bal    
acc1=Acc(10000,12345)
acc1.debit(1000)
acc1.credit(5000)
acc1.debit(4000)
acc1.debit(2000)










