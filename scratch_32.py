phone_balance=10
bank_balance=50
if phone_balance<100:
    phone_balance+=10
    bank_balance-=10

print(phone_balance)
print(bank_balance)

number=1565
if number%2==0:
    print("Number"+str(number)+"is even.")
else:
    print("Number"+str(number)+"is odd.")

#Third Example - try to change the value of age
age = 35
# Here are the age limits for bus fares
free_up_to_age = 4
child_up_to_age = 18
senior_from_age = 65

# These lines determine the bus fare prices
concession_ticket = 1.25
adult_ticket = 2.50

if age<=free_up_to_age:
    ticket_price=0
elif age<=child_up_to_age:
    ticket_price=concession_ticket
elif age>=senior_from_age:
    ticket_price=concession_ticket
else:
    ticket_price=adult_ticket

message="Somebody who is{} years old will pay{} to ride the bus.".format(age,ticket_price)
print(message)

points=174
if points<=50:
    results="congralutions! You won a wooden rabbit!"
elif points<=150:
    results="Oh dear,no prize this time."
elif points<=180:
    result="Congralutions! You won a wafer-thin  mint!"
else:
    result="Congralutions! You won a penguin!"
print(result)