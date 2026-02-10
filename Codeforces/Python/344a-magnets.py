def main():
    n = int(input())
    groups, prev = 0, 0
    for _ in range(n):
        magnet = int(input())
        # If the previous magnet value is not the same as current magnet value, a new group has started and this statement
        # will not execute until a magnet with opposite pattern comes, and there are only 10 and 01 patterns as input
        if prev != magnet:
            groups += 1
        # Keep on changing prev with current value to see if the next value is part of the group or not
        prev = magnet
    print(groups)


if __name__ == "__main__":
    main()
