def main():
    s = input()
    upper, lower = 0, 0
    for char in s:
        if char.isupper():
            upper += 1
        else:
            lower += 1

    # If there are more uppercase characters than lowercase, we print s in uppercase
    if upper > lower:
        print(s.upper())
    # Else if uppercase and lowercase char are equal or there are more lowercase char than uppercase, we print s in lowecase
    else:
        print(s.lower())


if __name__ == "__main__":
    main()
