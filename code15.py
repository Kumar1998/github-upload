num = int(input("Enter a number:"))
sum=0
numdup=num
while numdup > 0:
    i=numdup % 10
    sum+=i*i*i
    numdup=numdup//10
if sum==num:
    print("Armstrongnumber")
else:
    print("Not an armstong number")