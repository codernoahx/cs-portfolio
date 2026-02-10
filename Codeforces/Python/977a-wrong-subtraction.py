def main():
    n, k = map(int, input().split())
    # Keep on iterating until k becomes 0
    while k:
        # Gives us the right most digit, If it's non-zero we sub 1 from n
        if n % 10 != 0:
            n -= 1
        # Else remove the last digit
        else:
            n //= 10
        # After each iteration sub 1 from k
        k -= 1
    print(n)
    

if __name__ == "__main__":
    main()