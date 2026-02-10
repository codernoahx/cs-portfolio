# Part A: House Hunting


def main():
    # Divide the annual salary by 12 and store it in monthly_salary
    monthly_salary = int(input("Enter your annual salary: ")) / 12
    # Percent of the salary you wish to save
    portion_saved = float(
        input("Enter the percent of your salary to save, as a decimal: ")
    )
    # Take the 25% of your dream house total cost as portion for down payment
    portion_down_payment = int(input("Enter the cost of your dream home: ")) * 0.25
    # The current savings start with 0, and the annual savings return is 4%
    current_savings, r = 0, 0.04
    # Number of months to keep track of how many months it'll take to gather enough money for down payment
    number_of_months = 0

    # Keep on iterating until current_savings is less than portion for down payment
    while portion_down_payment > current_savings:
        # curren_savings + monthly salary's 4% + current saving's annual investment return of 4% divided by 12
        # for monthly calculation
        current_savings += (monthly_salary * portion_saved) + (
            (current_savings * r) / 12
        )
        # After each iteration increments number of months by 1
        number_of_months += 1

    # Print the number of months needed
    print(f"Number of months: {number_of_months}")


if __name__ == "__main__":
    main()
