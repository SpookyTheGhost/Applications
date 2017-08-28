# need to update IRS bracket amounts for current year, this is for 2016

print("Welcome to automated federal taxes")
print("""MENU
------------------------
single: s
married: m
separate married:sm
widow: w
""")
filingType = input("Please choose an option from the menu: ").lower()
income = float(input("What is your total income, number only: "))

print("for simplicity, standard deduction is used over itemized deduction")
while (filintType != 's' or filintType != 'sm' or filintType != 'm' or filintType != 'w'):
	print("Invalid selection, try again")
	filingType = input("Please choose an option from the menu: ").lower()
else:
	# reducing by standard deduction
	if filingType == "s" or filingType == "sm":
		indicator = False # cancel the reprompt
		income -= 6300
	elif filingType == "m" or filingType == "w":
		indicator = False # cancel the reprompt
		income -= 12600

# FICA 
medicare = income * 0.0145
SocialSecurity = 0
if (income > 118500):
    SocialSecurity += 118500 * 0.062 
else:
    SocialSecurity += income * 0.062
	
print("Medicare amount: ", medicare)
print("Social Security amount: ", SocialSecurity)

print("Begining to calculate based on recent tax tables")
def bracket(income, total1, total2, rate, n):
	taxOwed = 0
	if (income < total1):
		pass
	elif (income >= total1 and income < total2):
		taxOwed = (income - total1)*rate
	else:
		taxOwed = (total2 - total1)*rate
	output = "bracket " + str(n) + ": " + str(taxOwed)
	print(output)
	return taxOwed

total = 0.0
total += bracket(income, 0, 9275, 0.10, 1) # bracket 1
total += bracket(income, 9275, 37650, 0.15, 2) # bracket 2
total += bracket(income, 37650, 91150, 0.25, 3) # bracket 3
total += bracket(income, 91150, 190150, 0.28, 4) # bracket 4
total += bracket(income, 190150, 413350, 0.33, 5) # bracket 5
total += bracket(income, 413350, 415050, 0.35, 6) # bracket 6
total += bracket(income, 415050, 2147483647, 0.396, 7) # bracket 7
print("total is: ", total)

