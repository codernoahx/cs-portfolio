from collections import Counter


def main():
    guest_name = input()
    host_name = input()
    pile_of_letters = input()
    # IF we count all the letters in guest and host, and store them as dict: alphabet -> appeared
    # Now if we do the same thing with pile of letters, and then compare both the dict and if they're the same
    # print YES else NO. (Dict can be compared, and if all the keys and vals match it means they're  the same,
    # It evaluates to True, else False if either key or vals or both don't match)
    if Counter(guest_name + host_name) == Counter(pile_of_letters):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
