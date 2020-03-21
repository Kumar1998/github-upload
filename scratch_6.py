d1={'Canada':100,'Japan':200,'Jaipur':300,'Italy':400}
for key in sorted(d1):
    print("%s:%s"%(key,d1[key]))

tuple1=("India","Canada","Japan","Italy")

print(tuple1[0])
print(tuple1[2])

testtuple=("India","Canada","Japan","Italy")

for item in testtuple:
    print(item)

testtuple=("India","Canada","Japan","Italy")
del testtuple

tuples=(0,1,2,3,4,5,6,7,8,9)
print(tuples[4:])  #From index 4 to last index
print(tuples[:4])  #From index 0 to 4 index
print(tuples[4:7])  #From index 4(included) up to index 7(included)
print(tuples[1::])   #Excluded First item
print(tuples[:-1])  #Excluded last item
print(tuples[:-2])    #Upto second last index(negative index)
print(tuples[::-1])   #From last to first in reverse order [negative step]
print(tuples[::-2])    #All odd numbers in reversed order
print(tuples[-2::-2])  #All even numbers in reversed order
print(tuples[::])      #All items

countrylist=("India","Canada","Japan","Italy")
ind,itl,jap,itl=countrylist
print(ind)
print(itl)
