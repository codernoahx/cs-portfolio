def main():
    n, h = map(int, input().split())
    heights = input().split()
    width = 0

    for height in heights:
        # If the height is greater than h, it means the person has to bend and their width size will be 2
        if int(height) > h:
            width += 2
        # Else if the height is equal to or less than h, which means they don't have to bend, so their width size will be 1
        else:
            width += 1
    print(width)


if __name__ == "__main__":
    main()
