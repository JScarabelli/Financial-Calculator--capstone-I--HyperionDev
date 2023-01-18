# compulsory task 1

# importing math library
import math

# displaying the initial investment options.
print("Choose either 'investment' or 'bond' from the menu below to proceed:\n ")
print("Investment\t - to calculate the amount of interest you'll earn on your investment.")
print("bond\t\t - to calculate the amount you'll have to pay on a home loan.\n")

# requesting the user's input to continue.
user = input("Please choose one of either option to continue: ").lower()

# creating a while loop to determine which type of investment the user wants investment or bond.
while True:
    if user == "investment":
        invest = float(input("Please enter your deposit amount: £ "))
        interest_rate = int(input("Please enter the interest rate: "))
        interest_percentage = (interest_rate/100)
        years = float(input("Please enter how many years you plan to invest: "))
        interest = input("Please choose either compound or simple interest: ").lower()

        # creating a while loop to determine which type of return the user wishes simple or compound.
        # calculating the return on the user's option.
        if interest == "simple":
            print(f"Your investment return in a simple interest rate is £{invest*(1+interest_percentage*years)} ")
            break
        elif interest == "compound":
            print(f"Your investment return in a compound rate is £{round(invest * math.pow((1 + interest_percentage),years))}")
            break
        else:
            interest = input("Please choose either compound or simple interest: ").lower()
            continue

    # requesting the user to input info for the loan
    # calculating the monthly repayment
    if user == "bond":
        present_value = float(input("Please enter the present value of the house: £ "))
        bond_interest = int(input("Please enter the interest rate: "))
        bond_interest_percentage = float((bond_interest/100)/12)
        numbers_of_months = int(input("Please enter the number of months you wish for repayment: "))
        print(f"Your monthly repayment would be £{round((bond_interest_percentage*present_value)/ (1-(1+bond_interest_percentage)**(-numbers_of_months)))}")
        break

    # while loop requesting the user to enter a valid option either investment or bond.
    else:
        user = input("Please choose a valid option to continue: ").lower()
        continue

