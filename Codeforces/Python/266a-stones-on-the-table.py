def main():
    n = int(input())
    s = input()

    # If there is only one stone, that means we can print 0
    if n == 1:
        print(0)
    # Else if there are more than 1, then we check if the previous color matches the ith color, we do +1, i.e, we have
    # to remove that stone from the sequence of string to make sure the neighbours have different colors.
    else:
        rem = 0
        for i in range(1, n):
            if s[i] == s[i - 1]:
                rem += 1
        print(rem)


if __name__ == "__main__":
    main()