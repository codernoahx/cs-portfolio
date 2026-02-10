def main():
    n, m = map(int, input().split())
    #  At beginning head won't be at start, that's why it's set to False
    head_at_start = False
    # i starts at 0
    for i in range(n):
        # If remainder is 0, then # else .
        char = "#" if i % 2 == 0 else "."
        # If head_at_start is True print #
        if head_at_start:
            print("#", end="")
        # Print char till m - 1, because which ever head_at_start statement executes it'll give us the missing #
        # In both . and # case, since we need one more char to fill up the (m - 1)th space
        for _ in range(m - 1):
            print(char, end="")
        # Else if the head_at_start is False, print #
        if not head_at_start:
            print("#", end="")
        # If the char printed was "." then reverse the value of head_at_start
        # Essentially we want the head at_start conditionals to execute alternatively
        if char == ".":
            head_at_start = not head_at_start
        print()
    
    
if __name__ == "__main__":
    main()