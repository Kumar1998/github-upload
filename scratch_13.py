#python code to demonstrate the working of zip()
name=["Karan","Pratik","Justin","Mark"]
roll_no=[4,2,3,6]
marks=[60,89,97,76]

#using zip() to map values
mapped=zip(name,roll_no,marks)

#converting values to print as set
mapped=set(mapped)

#printing resultant values
print("This zipped result is:",end="")
print(mapped)
