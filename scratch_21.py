def foo(a,b):
    if a==b:
        return (a+b)*2
    else:
        return a+b

x=foo(1,3)
y=foo(2,2)
print(x,y)

def foo(a,b):
    if a+b in range(10,15):
        return 20
    else:
        return a+b
x=foo(9,5)
y=foo(9,6)
foo(x,y)
print(x,y)
