print(True or False)
print(True and False)

n=5 #number of levels for free
for level in range(1,n+1):
    print(level * '*')
for level in range(1,n+1):
    print(''*(n-level)+ level* '*')

print(len("Hello")+len("World"))

a={'d':3}
print(a.get('d'))
a['d']+=2
print(a.get('d')+3)

temp=35
if temp>30:
    print("Hot!")
elif temp>10:
    print("Warm")
else:
    print("cold")
