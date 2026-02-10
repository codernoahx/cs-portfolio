def main():
    m, n = map(int, input().split())
    # Board is of m * n size and domino size is 2 * 1, we just have to divide(integer/floor division) the board size by domino size(2).
    print((m * n) // 2)


if __name__ == "__main__":
    main()
