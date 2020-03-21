class Base():
    def hi(self):
        return 5
class child(Base): #extending
    def hello(self):
              return 6
c=child()
#access child class object
print(c.hello())

#you can access parent class objects
#because of inheritance
print(c.hi())

