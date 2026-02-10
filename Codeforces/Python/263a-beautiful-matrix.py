def main():
    # We loop 5 times for 5 rows
    for i in range(5):
        # We store the ith row/list in a temp variable
        temp = list(map(int, input().split()))
        # We look for the index of value 1 in temp, if it doesn't exist it throws ValueError
        try:
            c = temp.index(1) + 1  # +1 because it's 0-indexed
            r = i + 1  # +1 because it's 0-indexed
        # We catch the error and continue with loop
        except ValueError:
            continue

    # We need to know the moves needed to bring 1 at the middle of 5x5 matrix. We sub 3 from both the row and col position of 1
    # and add them together, before adding use absolute function on the subs of row and col position of 1.
    print(abs(3 - r) + abs(3 - c))


if __name__ == "__main__":
    main()
