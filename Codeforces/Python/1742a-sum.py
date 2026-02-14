def main():
    t = int(input())
    for _ in range(t):
        a, b, c = map(int, input().split())
        # If the sum of any two numbers is equal to the one which is left, then print YES else NO
        if a + b == c or b + c == a or c + a == b:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    main()
