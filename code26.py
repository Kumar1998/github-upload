#Take an input, convert it into an int, store it in num
num=int(input("Enter a number:"))
#Needs to be 1 at first , 'cause we're going to multiply
result=1
#Check if the number is negative
if num<0:
     print("Factorial doesn't exist")
#Check if the number is zero
elif num==0:
    print("The factorial is zero i one")

#So,num is positive
else:
    for i in range (1,num+1):
        result=result*i #Multiply number from 1 to num
    print("The factorial of",num,"is",result)