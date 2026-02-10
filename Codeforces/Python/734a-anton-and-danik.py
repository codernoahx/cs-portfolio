from collections import Counter


def main():
    n = int(input())
    # Makes a dict, which holds the count of the number of char repetitions in the string for a particular char
    s = Counter(input())

    if s["A"] > s["D"]:
        print("Anton")
    elif s["D"] > s["A"]:
        print("Danik")
    else:
        print("Friendship")


if __name__ == "__main__":
    main()
