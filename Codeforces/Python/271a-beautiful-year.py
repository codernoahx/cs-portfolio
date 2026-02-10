def main():
    y = int(input())

    # Keep on looping until we find the number
    while True:
        # We increment y by 1 and set num to y which is a temp variable
        num = y = y + 1
        # To keep track of the digits we have seen
        seen = []
        # Keep in iterating until num becomes 0
        while num:
            # Gets the right most digit
            ones = num % 10
            # If that digit exits in seen, we break the loop prematurely
            if ones in seen:
                break
            # Else we append that digit
            seen.append(ones)
            # And remove the ones digit from the num variable
            num //= 10
        # If the num digit value is 0, that means we never exited the inner while loop prematurely, i.e., we never found a value that
        # already existed in our seen list, meaning all the values in the seen are unique and thus num became 0 since we had to iterate
        # over every single digit to check if that digit existed in our seen or not. Since all the digits were unique, num became 0
        # that means we found a number with unique digits for which we iterated the whole number. That means we can break out of this
        # infinite loop
        if not num:
            break
    # print y since that was the number that managed to break the infinite loop
    print(y)


if __name__ == "__main__":
    main()
