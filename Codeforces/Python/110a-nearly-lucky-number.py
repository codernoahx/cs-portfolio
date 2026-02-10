def main():
    num = int(input())
    # To count the number of lucky digits
    lucky_num = 0
    # Until num becomes 0
    while num:
        # Extract the remainder or the last digit
        temp = num % 10
        # If it is 4 or 7 we increment it lucky_num count by 1
        if temp == 4 or temp == 7:
            lucky_num += 1
        # And remove the last digit from num after each iteration
        num = num // 10

    # If the count of luck_num is 4 or 7 then it is lucky number else, it isn't.
    if lucky_num == 4 or lucky_num == 7:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
