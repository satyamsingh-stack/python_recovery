class students():
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def add(self,a=None,b=None):
        x=a+b
        return x

s1=students(3,4)
print(s1.add(4,5))