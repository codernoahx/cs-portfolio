def main():
    a, b = map(int, input().split())
    years = 0

    # While a's weight is less than or equal to b, we'll keep looping
    while a <= b:
        a *= 3
        b *= 2
        years += 1
    print(years)


if __name__ == "__main__":
    main()
