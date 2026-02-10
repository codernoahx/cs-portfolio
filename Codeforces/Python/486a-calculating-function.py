def main():
    # The input and output has a relation: 1 -> -1, 2 -> 1, 3 -> -2, 4 -> 2
    n = int(input())
    # If n is even divide n by 2, because the output will be half of n
    if n % 2 == 0:
        print(n // 2)
    # Else if it is odd, then the output will be negative of n + 1 halved
    else:
        print(-(n + 1) // 2)


if __name__ == "__main__":
    main()
