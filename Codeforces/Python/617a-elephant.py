def main():
    n = int(input())
    steps = 0
    # Keep on looping until n becomes 0 or less
    # If n becomes 0 we have correct no. of steps, if it becomes -1, -2, -3, -4 we know this means it has to be sub by
    # 4, 3, 2 or 1 instead of 5 but still the number of steps won't change even if we make them -ve by sub them by 5
    # It's the same thing if at the end of sub we find the correct integer to sub them and then do +1. Our goal is
    # knowing correct number of steps not sub the correct elements to make it a perfect 0. Subtracting the max value,
    # helps us in finding the minimum possible moves and if the last move needs to be sub by something lower than 5 to make it 0
    # then we can just sub it by 5 instead and break the loop because that one step has to be added doesn't matter what we sub.
    while n > 0:
        steps += 1
        n -= 5
    print(steps)


if __name__ == "__main__":
    main()
