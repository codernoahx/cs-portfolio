def main():
    x, y, z = map(int, input().split())
    # The total distance that the 3 friends have to cover to reach mid-point will be, the distance from leftmost friend to
    # middle friends and the rightmost friend to middle friend. Since the they don't start at 0, we need to subtract leftmost
    # point with rightmost point in order to get the actual distance between leftmost and rightmost point and in between that
    # distance lies the mid-point
    print(max(x, y, z) - min(x, y, z))


if __name__ == "__main__":
    main()
