#number we"ll find the factorial of
number=6
#start with our product equal to one
product =1
#calculate factorial of number with a for loop
for num in range(2,number+1):
    product*=num

#print the factorial of the number
print(product)

letters=['a','b','c']
nums=[1,2,3]
for letter,num in zip(letters,nums):
    print("{}:{}".format(letters,num))

letters=['a''b''c','d','e']
for i,letter in enumerate(letters):
    print(i,letter)