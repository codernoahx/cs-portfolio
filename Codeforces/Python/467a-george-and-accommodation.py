def main():
    n = int(input())
    rooms = 0
    for _ in range(n):
        p, q = map(int, input().split())
        # If the difference is greater than or equal to 2, increment rooms by 1
        if q - p >= 2:
            rooms += 1
    print(rooms)


if __name__ == "__main__":
    main()
