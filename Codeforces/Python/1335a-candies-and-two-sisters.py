def main():
    t = int(input())
    res = []
    for _ in range(t):
        # Sub n by 1 and then halve it using integer division (to round it down) to get the correct
        # number of distinct ways to distribute n between 2 people
        n = (int(input()) - 1) // 2
        res.append(n)
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
