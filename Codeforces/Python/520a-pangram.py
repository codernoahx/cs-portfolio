from collections import defaultdict


def main():
    n = int(input())
    s = input()
    # We'll use hashmap to keep track of unique characters, stored as pair of char: bool
    hashmap = defaultdict(bool)
    # We loop through the lowercase string
    for char in s.lower():
        # And for each pair whether it exits or not in the hasmap we set it to True
        hashmap[char] = True

    # If len of hashamp is 26, that means it's a pangram else it's not
    print("YES" if len(hashmap) == 26 else "NO")


if __name__ == "__main__":
    main()
