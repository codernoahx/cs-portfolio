def main():
    # We split the input by "+"
    sum = input().split("+")
    # Sort the numbers as str type in non-decreasing order and join them as a string, separated by "+"
    print("+".join(sorted(sum)))


if __name__ == "__main__":
    main()
