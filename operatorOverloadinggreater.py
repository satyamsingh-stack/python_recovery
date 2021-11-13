class students():
    def __init__(self,m1):
        self.m1=m1


    def __gt__(self, other):
        if(self.m1>other.m1):
            return self.m1

m1=int(input("Enter value of m1:"))
n1=int(input("Enter value of n1:"))
x1=int(input("Enter va;ue of x1:"))
s1=students(m1)
s2=students(n1)
s3=students(x1)

if(s1>s2 and s1>s3):
    print(m1,"is greatest")
elif(s2>s1 and s2>s3):
    print(n1,"is greatest")
else:
    print(x1,"is greatest number")