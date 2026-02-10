def main():
    n = int(input())  # Number of bits sequences
    # Convert bits separated by space into list of lists with ints as elements: [[1, 1, 0], [0, 1, 0], [1, 0, 1]]
    # Loop for n times and each time we are expecting a sequence of bits of length 3.
    # Split the input by space and then use map convert the splitted elements to int type.
    # And finally converting the map object to a list type.
    confirmation = [list(map(int, input().split())) for _ in range(n)]
    res = 0
    for confirm in confirmation:
        # if there are 2 or more 1's in a list of 3 bits we have to increment res by 1. Ex: [1 + 1 + 0] == [2]
        if sum(confirm) >= 2:
            res += 1
    print(res)


if __name__ == "__main__":
    main()
