def main():
    l1 = input()
    l2 = input()
    res = ""

    for i in range(len(l1)):
        # Taking the modulo after adding will give 0 when answer is 2 or 0, in both cases the ith digit will be same 11 or 00
        # When they differ it'll become 1 and it's mod will be 1. And we'll add the expression result at the end of res, because
        # we're starting from index 0
        res += str((int(l1[i]) + int(l2[i])) % 2)
    print(res)


if __name__ == "__main__":
    main()
