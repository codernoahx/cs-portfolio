def main():
    x = 0

    for _ in range(int(input())):
        op = input().strip()
        # Increment by 1 if there's + in operation else decrement it by 1
        x += 1 if "+" in op else -1
    print(x)


if __name__ == "__main__":
    main()
