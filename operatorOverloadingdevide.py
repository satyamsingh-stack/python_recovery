class students():
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __floordiv__(self, other):
        n1=self.m1//other.m1
        n2=self.m2//other.m2
        s3=students(m1,m2)
        return s3

m1=int(input("Enter vlaue of m1:"))
m2=int(input("Enter value of m2:"))
n1=int(input("Enter value of n1:"))
n2=int(input("Enter value of n2:"))

s1=students(m1,m2)
s2=students(n1,n2)

s3=s1//s2
print(s3.m1//n1,s3.m2//n2)