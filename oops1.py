'''class Car:
    color="Black"
    def __init__(self,type):
        self.type=type
  
    @staticmethod
    def strt():
        print("strted")
    @staticmethod    
    def stop():
        print("stoped") 
class C(Car):
    def __init__(self,name,type):
        self.name=name
        super().__init__(type)
        super().strt()
car1=C("petrol","ele")
print(car1.type) '''




'''class A:
    a="Wellcom to class a "
class B:
    b="wellcom to class b"
class C(A,B):
    c="wellcom"
c1=C()
print(c1.a)
print(c1.b)
print(c1.c)'''

class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
    @property 
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3)+"%" 

s1=Student(45,43,46)
print(s1.percentage) 
s1.chem=45
print(s1.percentage)

