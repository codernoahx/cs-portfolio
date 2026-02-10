def main():
    res = []
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        # We want ceil of floor div. To do that without math.ceil function, we divide negative number with int div,
        # it returns the negative ceil value and we make it +ve with - sign
        q = -(-a // b)
        # We subtract the qth multiple of b with a, which tells us how many more numbers to add in order to make
        # a completely divisible by b
        res.append((q * b) - a)
        # * is used to unpack the list and then print it separated with newline
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
