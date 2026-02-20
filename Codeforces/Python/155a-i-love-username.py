def main():
    n = int(input())
    points = list(map(int, input().split()))
    amazing_performances, minimum, maximum = 0, points[0], points[0]
    for i in range(1, n):
        # Set minimum to ith point if the current minimum is larger than ith point
        # And increment amazing performances by 1
        if minimum > points[i]:
            minimum = points[i]
            amazing_performances += 1
        # And increment amazing performances by 1
        # Else set maximum to ith point if the current maximum is smaller than ith point
        elif maximum < points[i]:
            maximum = points[i]
            amazing_performances += 1
    print(amazing_performances)


if __name__ == "__main__":
    main()
