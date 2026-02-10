def main():
    k = int(input())
    l = int(input())
    m = int(input())
    n = int(input())
    d = int(input())
    damaged = 0
    for i in range(1, d + 1):
        # If any of the values of i is completely divisible by k, l, m, and n, increment damaged by 1
        if i % k == 0 or i % l == 0 or i % m == 0 or i % n == 0:
            damaged += 1
    print(damaged)


if __name__ == "__main__":
    main()
