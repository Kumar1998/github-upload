testList=["Canada","Japan","London","Germany","Africa"]

for item in testList:
    print(item)

testList=["Canada","Japan","London","Germany","Africa"]

if "Japan" in testList:
   print("Yes")

testList=["Canada","Japan","London","Germany"]
print (len(testList))

testList=["Canada","Japan","London","Germany"]
print (testList)

testList.append("SOUTHKOREA")
print (testList)

testList=["Canada","Japan","London","Germany"]
print (testList)

testList.remove("Japan")
print (testList)

testList.pop(1)
print (testList)

testList.pop()
print(testList)

testList=["Canada","Japan","London","Germany"]
testList.clear()
print (testList)

del testList

list1=["canada","japan"]
list2=["shanu","neha"]

list3=list1+list2
print(list)

mergedlist=[]
mergedlist.extend(list1)
mergedlist.extend(list2)
print(mergedlist)

testList=["canada","japan","London","germany","africa"]
print(testList[0]) #first item
print (testList[-1]) #last item

testList=["canada","japan","canada","germany","japan","italy"]
print (testList)

cleanlist=[]
[cleanlist.append(x) for x in testList if x not in cleanlist


print(cleanlist)

list1=["Canada","Japan","Canada","Germany","Japan","Italy"]
list2=["Germany","France","Poland","Italy","India","London"]
sub1=list(set(list)-set(list2))
print(sub1)

sub2=list(set(list2)-set(list1))
print(sub2)

import random

listsItems=["Canada","Japan","France","Germany","Italy","Poland"]

print(listItems)

random.shuffle(listItems,random.random)
print(listItems)

d1={}
d1[0]="canada"
d1[1]="japan"
print(d1)

d1={'Canada':100,'Japan':500}
x=d1["Canada"]
y=d1.get("Japan")
print(x)
print(y)

d1={'Canada':100,'Japan':500}
print(d1["Canada"])
d1["Canada"]=200
print(d1["Canada"])

d1={'Canada':100,'Japan':500}
print (d1)
d1["Germany"]=600
d1["Italy"]=400
print(d1)

d1={'Canada':100,'Japan':200,'Germany':300,'Italy':400}
d1.pop("Canada")
del d1["Germany"]
d1.popitem()
print(d1)