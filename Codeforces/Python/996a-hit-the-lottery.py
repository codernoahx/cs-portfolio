def main():
    n = int(input())
    bills = 0
    # Keep on looping until n is greater than equal to 5
    while n >= 5:
        # If n is greater than or equal to 100, subtract 100 from it
        if n >= 100:
            n -= 100
        # Else if n is greater than or equal to 20, subtract 20 from it
        elif n >= 20:
            n -= 20
        # Else if n is greater than or equal to 10, subtract 10 from it
        elif n >= 10:
            n -= 10
        # Else if n is greater than or equal to 5, subtract 5 from it
        elif n >= 5:
            n -= 5
        # After each iteration increment bills by 1
        bills += 1
    # The answer will be bills + n (which is 1 dollar bills from 4 to 0)
    print(bills + n)


if __name__ == "__main__":
    main()
