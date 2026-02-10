def main():
    word = input()
    # We convert the first char to upper case, since upper() returns a copy we concatenate the rest of the string with the copy
    # and print it
    print(word[0].upper() + word[1:])


if __name__ == "__main__":
    main()
