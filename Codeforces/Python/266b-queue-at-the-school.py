def main():
    n, t = map(int, input().split())
    # It is converted to list because strings are immutable in python
    s = list(input())

    # We will loop t times which is the number of swaps, we'll loop until t becomes 0
    while t:
        # Start at the first index
        i = 0
        # Keep on iterating until i is less than n - 1, because we'll be doing i + 1. Sp we need to make sure we don't go out of bounds
        while i < n - 1:
            # If the current letter is B and the next letter is G swap them
            if s[i] == "B" and s[i + 1] == "G":
                s[i], s[i + 1] = s[i + 1], s[i]
                # And increment by 2 because i is where we are currently G is at i + 1, we swapped them and they're at correct
                # position, now it's time to check for i + 2 letter in the list
                i += 2
            # Else increment i by 1
            else:
                i += 1
        # Decrement t by 1, as we have done 1 swap and now t - 1 swaps are left to do.
        t -= 1
    # Convert them back to string and print it
    print("".join(s))


if __name__ == "__main__":
    main()
