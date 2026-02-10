def main():
    # Sub the total cost of w bananas we need to buy with n initial dollars we have so that we know how much to borrow
    k, n, w = map(int, input().split())
    total_cost = 0
    # We loop for bananas from 1 to w (including)
    for i in range(1, w + 1):
        # The cost for ith banana is calculated by multiplying k by i
        total_cost += i * k
    # If total cost is greater than, we sub total cost with n and print it
    # Else if it is equal to n or less than n we print 0
    print(total_cost - n if total_cost > n else 0)


if __name__ == "__main__":
    main()
