class computer():
    def hardware(self):
        print("Dell Vostro 14 3000,intel Core i5, 8 GB ram, 1 tera byte storage")


comp1=computer()
computer.hardware(comp1)
comp2=computer()
computer.hardware(comp2)

# class mathmetics:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def add(self):
#         print(self.a+self.b)
#     def sub(self):
#         if(self.a<self.b):
#             print(self.b-self.a)
#         else:
#             print(self.a-self.b)
#     def mul(self):
#         print(self.a*self.b)
#     def floordiv(self):
#         if(self.a>self.b):
#             print(self.a//self.b)
#         else:
#             print(self.b//self.a)
# a,b=map(int,input().split())
# if(__name__=='__main__'):
#     m1=mathmetics(a,b)
#     m1.add()
#     m1.sub()
#     m1.mul()
#     m1.floordiv()