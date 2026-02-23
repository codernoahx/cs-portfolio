def main():
    n, k = map(int, input().split())
    total_time = 0
    # Keep on iterating from 1st till nth problem, because problems will start from 1 instead of 0
    for i in range(1, n + 1):
        total_time += 5 * i
        # If one of ith problem in the n number of problems, where k time + total time is more than 4hrs (240 mins)
        # That means we break the loop and subtract i by 1, because we don't have enough time to solve the
        # ith and rest of the n - i problems
        if k + total_time > 240:
            print(i - 1)
            break
    # If we the loop runs without breaking out prematurely, that means we never crossed the 240 mins mark
    # And thus we had enough time to solve all the n problems
    else:
        print(n)


if __name__ == "__main__":
    main()
