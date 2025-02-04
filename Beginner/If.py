#Determine the BMI category of user
height=float(input("Enter your height(in meters):"))
weight=float(input("Enter your weight(in kilograms):"))
BMI=weight/(height)**2
if (BMI>=30):
    print(f"You belong to the Obesity category")
elif (BMI<=29 and BMI>=25):
    print(f"You belong to the Overweight category")
elif (BMI>=18.5 and BMI<25):
    print(f"You belong to the normal category")
else:
    print(f"You belong to the underweight category")
#Determien which city belongs to which country
Australia=["Sydney","Melbourne","Brisbane","Perth"]
UAE=["Dubai","Abu Dhabi","Sharjah","Ajman"]
India=["Mumbai","Bangalore","Chennai","Delhi"]
city=str(input("Enter city name: "))
if city in UAE:
    print(f"{city} is in UAE")
elif city in India:
    print(f"{city} is in India")
elif city in Australia:
    print(f"{city} is in Australia")
else:
    print("City entered is not present in UAE,India,Australia")
#Determine if both cities are in the same country
city1, city2=input("Enter name of two cities:").split()
if (city1 in UAE and city2 in UAE):
    print("Both cities are in UAE")
elif (city1 in India and city2 in India):
    print("Both cities are in India")
elif (city1 in Australia and city2 in Australia):
    print("Both cities are in Australia")
else:
    print("They do not belong to the same country")

