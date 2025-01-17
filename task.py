print("Welcome to the tip calculator!")
bill=float(input("What was the total bill? $"))
tip= ((float(input("How much tip would you like to give? 10, 12, or 15? ")))*bill)/100
n_split=int(input("How many people to split the bill?"))
res= (bill + tip) / n_split
#print("Each person should pay: $" + str(res))
#amount to be paid by each person must be in decimal
print(f"Each person should pay: ${res:.2f}")
