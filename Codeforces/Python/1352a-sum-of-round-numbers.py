def main():
    t = int(input())
    # To store the lists of summands
    res = []
    for _ in range(t):
        n = int(input())
        # To store the summands of n. Ex: 5009 -> [9, 5000]
        summands = []
        # Power is used to keep track of number places
        power = 1
        # While n isn't 0
        while n:
            # If n isn't 0
            if n % 10:
                # Append last digit of n raised to power
                summands.append((n % 10) * power)
            # Remove last digit from n
            n //= 10
            # Multiply power by 10 to increase it's number place
            power *= 10
        # And append the whole summands list in res
        res.append(summands)
    for ans in res:
        # Print no. of summands we got for n (we're not storing n, because it's not needed in ques) and the print all the summands
        print(len(ans))
        print(*ans)


if __name__ == "__main__":
    main()
