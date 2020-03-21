'''Nested looops with list comprehension'''

x,y,new=[1,2],[5,8],[]
for i in x:
    for j in y:
        new.append(i+j)
print(new)
#[6,9,7,10]

#List Comprehension 1 line code
[i+j for i in x for j in y]
#[6,9,7,10]