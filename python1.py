height=float(input("Enter height of the person:"))
weight=float(input("Enter weight of the person:"))
# the formula for calculating bmi
bmi=weight/(height**2)
print("Your BMI IS:{0} and you are:".format(bmi),end='')
#conditions
if(bmi<16):
    print("severly underweight")
elif(bmi>=16 and bmi<18.5):
    print("underweight")
elif(bmi>=18.5 and bmi>=25):
    print("underweight")
elif(bmi>=18.5 and bmi<25):
    print("healthy")
elif(bmi>=25 and bmi<30):
    print("overweight")
elif(bmi>=30):
    print("severly overweight")
import time
time.sleep(30)
