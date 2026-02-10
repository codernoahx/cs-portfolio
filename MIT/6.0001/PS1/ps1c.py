# Part C: Finding the right amount to save away


def main():
    annual_salary = int(input("Enter your annual salary: "))
    # Take the 25% of your $1M dream house total cost as portion for down payment
    portion_down_payment = 1000000 * 0.25
    # Divide the annual salary by 12 and store it in monthly_salary
    monthly_salary = annual_salary / 12
    # The annual savings return is 4%, and the salary increase percentage after every 6 months is 7%
    r, semi_annual_raise = 0.04, 0.07
    # 36 months time is the time needed to save money for the house downpayment, and number of bisection steps it took
    # to find the best savings rate.
    number_of_months, steps = 36, 0
    # For our search space, we use 0 to 10000 is to account for two additional decimal places in the range 0% to 100%.
    # We'll set savings_rate to 1.0 to see if we save 100% will we be able to save money for down payment
    low, high, savings_rate = 0, 10000, 1.0
    # If we save full salary for number of months (36) and still it's less than down payment, then execute this statement
    if portion_down_payment > calculate_savings(
        monthly_salary,
        number_of_months,
        savings_rate,
        r,
        semi_annual_raise,
    ):
        print("It is not possible to pay the down payment in three years.")
    else:
        # Keep on iterating until low is less than or equal too high
        while low <= high:
            # Calculate mid using int division and convert it to into savings rate using float division
            # to account for two additional decimal places in % (Ex: 43.21)
            mid = (low + high) // 2
            savings_rate = mid / 10000
            # Calculate current savings
            current_savings = calculate_savings(
                monthly_salary, number_of_months, savings_rate, r, semi_annual_raise
            )
            # If the difference is less than or equal too 100, that's the best savings rate, there can be multiple
            # savings rate but we just have to print the first one we encounter
            if abs(portion_down_payment - current_savings) <= 100:
                break
            # If current savings is less than down payment, set low to mid
            elif portion_down_payment > current_savings:
                low = mid
            # Else if current savings is greater than or equal too down payment set high to mid (But if that equal case exists,
            # we'll catch that when we'll look for difference between down payment and current savings)
            else:
                high = mid
            # Increment step by 1
            steps += 1
        print(f"Best savings rate: {savings_rate}")
        print(f"Steps in bisection search: {steps}")


def calculate_savings(
    monthly_salary,
    number_of_months,
    savings_rate,
    r,
    semi_annual_raise,
):
    # Current savings starts from 0
    current_savings = 0
    # We'll calculte savings for number of months, starting from 1 and including number of months
    for i in range(1, number_of_months + 1):
        # Add the monthly salary savings portion and the monthly portion of the annual savings return
        current_savings += (monthly_salary * savings_rate) + (
            (current_savings * r) / 12
        )
        # After every six months, increment the monthly salary by semi annual raise % of the monthly salary
        if i % 6 == 0:
            monthly_salary += monthly_salary * semi_annual_raise
    # return the calculated current savings
    return current_savings


if __name__ == "__main__":
    main()
