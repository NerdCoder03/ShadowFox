# creating a list of names and creating a list of tuples
names=['Arun','Varun','Raju','Sam','Sonakshi','Asha']
print(f"The list with my friend's names:{names}")
names_tuple=[]
for item in names:
    names_tuple.append((item,len(item)))
print(f"The tuple list with length of the names included with the names:\n{names_tuple}")

#Dictionary
my_expenses={"Hotel":1200,
             'Food':800,
             "Transportation":500,
             "Attractions":300,
             "Miscellaneous":200}
partner_expenses={"Hotel":1000,
             'Food':900,
             "Transportation":600,
             "Attractions":400,
             "Miscellaneous":500}
print(f"my_expenses:{my_expenses}")
print(f"partner_expenses:{partner_expenses}")
#calculate total expenses
my_expenses_total=sum(my_expenses.values())
partner_expenses_total=sum(partner_expenses.values())
print(f"My total expenses:{my_expenses_total} rupees")
print(f"Partner's total expenses:{partner_expenses_total} rupees")
#print who spent more
if my_expenses_total>partner_expenses_total:
    print("I spent more!")
elif partner_expenses_total>my_expenses_total:
    print("Partner spent more!")
else:
    print("Expenses are equal for both!")
#to find out where there was a significant difference in expenses
print("There was a significant difference in the expenses of the following categories:")
for category in my_expenses.keys():
    difference=abs(my_expenses[category]-partner_expenses[category])
    if difference>100:
        print(f"In {category} there is a significant difference of {difference} rupees.")
