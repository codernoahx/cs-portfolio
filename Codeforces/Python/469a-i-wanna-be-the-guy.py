def main():
    n = int(input())
    # Below we store the first input from the list in x/y and the rest in *p/*q,
    # used to capture a variable number of elements into a single list.
    x, *p = map(int, input().split())
    y, *q = map(int, input().split())
    # If the len of set of p + q list is equal to n we beat the game, else we didn't
    print("I become the guy." if len(set(p + q)) == n else "Oh, my keyboard!")


if __name__ == "__main__":
    main()
