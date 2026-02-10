def main():
    s = input()
    t = input()
    # If the reverse of s == t then print YES else NO
    print("YES" if s[::-1] == t else "NO")


if __name__ == "__main__":
    main()
