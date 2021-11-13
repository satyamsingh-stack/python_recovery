class A:
    def show(self):
        print("Hi!")

class B(A):
    pass
    # def show(self):
    #     print("Hello!")

a1=B()
a1.show()
a2=A()
a2.show()