def main():
    n = int(input())
    cur_psng, min_cap = 0, 0
    for _ in range(n):
        a, b = map(int, input().split())
        # Keep track of current passengers in the train by removing 'a' passengers exiting the tramp and adding 'b'
        # passengers entering the tramp
        cur_psng += b - a
        # Assign the greatest value between min_cap and cur_psng
        min_cap = max(min_cap, cur_psng)

    print(min_cap)


if __name__ == "__main__":
    main()
