# print("Welcome to the tip calculator!")
# bill = input("What was the total bill? $")
# tip = input("What percentage tip would you like to give? 10, 12 or 15? ")
# people_to_split = input("How many people to split the bill? ")
# payment = (float(bill) * ((int(tip) / 100) + 1))  / int(people_to_split)
# print(f"Each person should pay: ${round(payment, 2)}")

##CORREÇÃO DA ÂNGELA
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))
payment = (bill * (tip / 100 + 1)) / people
print(f"Each person should pay: ${round(payment, 2)}")