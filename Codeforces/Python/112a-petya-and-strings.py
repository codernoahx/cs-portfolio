def main():
    # Convert both inputs to lowercase
    s1 = input().lower()
    s2 = input().lower()
    # We are finding the first occurence of an alphabet which is different from the other string, if it exists. Based on
    # it's lexographical value we execute the conditionals and print the result.

    # If the first occurence of diff alphabet in s1 is greater lexicographically compared to s2, we print 1
    if s1 > s2:
        print(1)
    # Else if the first diff occurence of s2 alphabet is greater than s1, we print -1
    elif s2 > s1:
        print(-1)
    # Else they're exactly same, we print 0
    else:
        print(0)


if __name__ == "__main__":
    main()
