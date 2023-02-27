# This program allows a user to access two different financial calculators:
# an investment calculator and a loan repayment calculator.

# Begin by importing the math module.
import math

# Allow the user to choose between the investment or repayment calculator.
print("Choose either 'Investment' or 'Loan' from the menu below to proceed.\n"
      "Investment: Calculate the amount of interest you will earn on your investment.\n"
      "Loan: Calculate and plan your repayments on a loan product.")
while True:
    try:
        calculation_type = input("\nEnter your selection here: ").lower()

        # Where the investment calculator is selected, request the principal amount, interest rate,
        # and investment timeframe.
        if calculation_type == "investment":
            principal = float(input("Enter the amount to be deposited: "))
            rate = float(input(f"Enter the percentage interest rate, e.g. 8 for 8%: "))/100
            time = float(input("How many years do you plan on investing?: "))

            if principal <= 0:
                print("\nError: Negative investment amount.")
                break
            else:
                pass

            # Allow the user to select between a compound or simple interest calculation.
            # Calculate and display the total return depending on the user's selection.
            while True:
                interest = input("Preferred interest type? Simple or Compound: ").lower()
                if interest == "simple":
                    total_amount = principal * (1 + rate * time)
                    print(f"The total return for this investment is {total_amount:,.2f}.")
                    break
                elif interest == "compound":
                    total_amount = principal * (math.pow((1 + rate), time))
                    print(f"The total return for this investment is {total_amount:,.2f}.")
                    break

                # Display an error message if the user does not select a compound or simple calculation.
                else:
                    print("Enter 'Simple' or 'Compound'.")
                    continue
            break

        # Where the user wishes to make a repayment calculation, request the present loan value,
        # interest rate, and repayment timeframe.
        # Calculate and display the monthly repayments.
        elif calculation_type == "loan":
            value = float(input("Enter the amount you wish to borrow: "))
            rate = float(input("Enter the annual interest rate, e.g. 3.5 for 3.5%: "))/100
            rate = rate/12
            time = int(input("Spread repayments over how many months?: "))

            if value <= 0:
                print("\nError: Negative loan value.")
                break
            else:
                pass

            monthly_repayment = (rate * value) / (1 - (1 + rate) ** (-time))
            print(f"The amount payable monthly is {monthly_repayment:,.2f}")
            break

        # Display an error message if the calculation type is not selected correctly.
        else:
            print("Enter 'Investment' or 'Loan'.")
            continue

    # Manage any value errors with an error message.
    except ValueError:
        print("Verify input.")
