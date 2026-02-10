def main():
    n = int(input())
    opinions = map(int, input().split())
    # If there is at least one '1' in opinions then the problem is Hard else it's easy
    print("Hard" if 1 in opinions else "Easy")


if __name__ == "__main__":
    main()
