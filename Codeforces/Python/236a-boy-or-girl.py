def main():
    # To find distinct char in username we convert it to a set
    username = set(input())
    # If the len of distinct char set is even, it's female
    if len(username) % 2 == 0:
        print("CHAT WITH HER!")
    # Else if it's odd, it's male
    else:
        print("IGNORE HIM!")


if __name__ == "__main__":
    main()
