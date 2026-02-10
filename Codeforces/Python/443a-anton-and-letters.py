def main():
    s = input()
    # If there is nothing between {} then print 0
    if s == "{}":
        print(0)
    # Else remove opening and closing curly braces - {}. And the split it with comma + space because that's how elements are
    # separated and then convert that into a set and print it's len
    else:
        s = s[1 : len(s) - 1].split(", ")
        print(len(set(s)))


if __name__ == "__main__":
    main()
