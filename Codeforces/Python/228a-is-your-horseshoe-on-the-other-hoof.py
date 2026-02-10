def main():
    # Convert the input to set to remove duplicates, then find the len of the set and subtract 4 from it. Because the input will
    # always have 4 values. If there will be duplicates that means it's size will decrease and we need to fill up the rest of the
    # element spots in our input of len 4
    print(4 - len(set(input().split())))


if __name__ == "__main__":
    main()
