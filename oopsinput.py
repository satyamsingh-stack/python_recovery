class students():

    def __init__(self,name,branch,sec,m1,m2,m3):
        self.name=name
        self.branch=branch
        self.sec=sec
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def percentage(self):
        m=(self.m1+self.m2+self.m3)/3
        print(m,"%")

name=input("Enter your name:")
branch=input("Enter your branch:")
sec=input("Enter your section:")
m1=int(input("Enter marks obtain in Physic"))
m2=int(input("Enter marks obtain in maths:"))
m3=int(input("Enter marks obtain in chemistery:"))
s1=students(name,branch,sec,m1,m2,m3)
print("Name",name,"branch",branch,"sec",sec,"physic",m1,"maths",m2,"chemistery",m3)
print(s1.percentage())
