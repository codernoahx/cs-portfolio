def main():
    # How many words the user wants to input
    n = int(input())
    # Empty list that will contain words
    words = []
    for _ in range(n):
        words.append(input())

    # loop and print the results
    for word in words:
        # Words greater than 10 should get special abbreviation
        if len(word) > 10:
            print(word[0] + str(len(word[1:-1])) + word[-1])
        else:
            print(word)


if __name__ == "__main__":
    main()
