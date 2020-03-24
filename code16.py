num=input(("enter a number:"))
st=0
for i in num:
    st+=int(i)**3

if st==int(num):
    print("Armstrong number")
else:
    print("Not an armstrong")