class A:
    def foo(self):
        print('A')

class B:
    def foo(self):
        print('B')

#C class inherits A and B class respectively
class C(A,B):
    def __init__(self):
       super(c,self).foo() #this way
       super().foo()       #or this

c=(C)
A
A
