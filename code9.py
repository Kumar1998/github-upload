class MyInteger:
    def __init__(self,value):
        self.value=value
    def __repr__(self):
        return str(self.value+3)

i=MyInteger(4)
print(i)
        