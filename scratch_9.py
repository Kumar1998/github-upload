A=[1,2,3,4,5,6]
B=[1,2,3,4,5,6]

id(A)
id(B)

Angkorwat=(13.14125,103.86667)
print(type(Angkorwat))
print("AngkorWat is at latitude:{}".format(Angkorwat[0]))
print("Angkorwat is at longitude:{}".format(Angkorwat[1]))

dimensions={40,52,100}
length,width,height=dimensions
print("The dimensions are {}*{}*{}".format(length,width,height))

countries={'Angola','Maldives','India','Sweden','Finland'}
print((len(countries)))

numbers=[1,8,9,10,11,11,9,10]
unique_nums=set(numbers)
print(unique_nums)

fruit={"apple","banana","orange","grapefruit"}#define a set
print("watermelon"in fruit)#check for element

fruit.add("watermelon")#add an element
print(fruit)

print(fruit.pop())#remove a random element
print(fruit)

a=[1,2,2,3,3,3,4,4,4,4]
b=set(a)
print(len(a)-len(b))

elements={"hydrogen":1,"helium":2,"carbon":6}
print(elements["carbon"])
print("carbon"in elements)
print(elements.get("dilithium"))

elements={'hydrogen':1,'helium':2,'carbon':6}
x=elements.get('dilithium')
not_null=x is not None
print(not_null)

elements = {"hydrogen": {"number": 1,
                         "weight": 1.00794,
                         "symbol": "H"},
              "helium": {"number": 2,
                         "weight": 4.002602,
                         "symbol": "He"}}
helium = elements["helium"]  # get the helium dictionary
hydrogen_weight = elements["hydrogen"]["weight"]  # get hydrogen's weight
oxygen={"number":8,"weight":15.999,"symbol":"0"}
#create a new oxygen dictionary
elements["oxygen"]=oxygen #assign'oxygen' as a key to the the elements dictionary
print('elements=',elements)

phone_balance=3
bank_balance=100
print(phone_balance,bank_balance)
if phone_balance<5:
    phone_balance+=10
    bank_balance-=10
print(phone_balance,bank_balance)




