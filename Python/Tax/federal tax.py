print("Welcome to automated federal taxes\n")

print("Reference your W2 form to complete this\n")

print("""MENU
------------------------
single: s
married: m
separate married:sm
widow: w
""")

filingType = input("Please choose an option from the menu: ").lower()
print(filingType)
while (not(filingType == "s" or filingType == "sm" or filingType == "m" or filingType == "w")):
    print("Invalid selection, try again")
    filingType = input("Please choose an option from the menu: ").lower()
    
wages = input("What is your total income, number only: ")
try:
    income = float(wages)
except ValueError:
    wages = input("What is your total income, number only: ")
    
taxWithheld = input("How much taxes was with-held by employer, number only: ")
try:
    paidTax = float(wages)
except ValueError:
    taxWithheld = input("What is your total income, number only: ")
    
print("for simplicity, standard deduction is used over itemized deduction")


# reducing by standard deduction
if filingType == "s" or filingType == "sm":
        income -= 6300
elif filingType == "m" or filingType == "w":
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

totalOwed = 0.0
if filingType.lower() == "s":
    totalOwed += bracket(income, 0, 9325, 0.10, 1) # bracket 1
    totalOwed += bracket(income, 9325, 37950, 0.15, 2) # bracket 2
    totalOwed += bracket(income, 37950, 91900, 0.25, 3) # bracket 3
    totalOwed += bracket(income, 91900, 190650, 0.28, 4) # bracket 4
    totalOwed += bracket(income, 190650, 416700, 0.33, 5) # bracket 5
    totalOwed += bracket(income, 416700, 418400, 0.35, 6) # bracket 6
    totalOwed += bracket(income, 418400, 2147483647, 0.396, 7) # bracket 7

elif filingType == 'm' or filintType == 'w':
    totalOwed += bracket(income, 0, 18650, 0.10, 1) # bracket 1
    totalOwed += bracket(income, 18650, 75900, 0.15, 2) # bracket 2
    totalOwed += bracket(income, 75900, 153100, 0.25, 3) # bracket 3
    totalOwed += bracket(income, 153100, 233350, 0.28, 4) # bracket 4
    totalOwed += bracket(income, 233350, 416700, 0.33, 5) # bracket 5
    totalOwed += bracket(income, 416700, 470700, 0.35, 6) # bracket 6
    totalOwed += bracket(income, 470700, 2147483647, 0.396, 7) # bracket 7

elif filingType == 'sm':
    totalOwed += bracket(income, 0, 9325, 0.10, 1) # bracket 1
    totalOwed += bracket(income, 9326, 37950, 0.15, 2) # bracket 2
    totalOwed += bracket(income, 37951, 76550, 0.25, 3) # bracket 3
    totalOwed += bracket(income, 76551, 116675, 0.28, 4) # bracket 4
    totalOwed += bracket(income, 116676, 208350, 0.33, 5) # bracket 5
    totalOwed += bracket(income, 208351, 235350, 0.35, 6) # bracket 6
    totalOwed += bracket(income, 235350, 2147483647, 0.396, 7) # bracket 7
print("totalOwed tax owed is: ", totalOwed)

if totalOwed - paidTax >= 0:
    print("You owe the following amount: ", totalOwed - paidTax)
else:
    print("You overpaid the following amount: ", totalOwed - paidTax)
