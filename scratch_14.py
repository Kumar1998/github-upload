a=[1,2,3,4]
b=a
a+=[5,6]
print(b) #[1,2,3,4,5,6]
print(a) #[1,2,3,4,5,6]
#Does the inplace modification
#therefore both a and b changes
c=[1,2,3,4]
d=c
d=d+[5,6]
# d creates a new list and changes
#"d" reference to new list,while
#"c" still refer to old list
print(d) #[1,2,3,4,5,6]
print(c) #[1,2,3,4]