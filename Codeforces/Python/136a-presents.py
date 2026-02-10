def main():
    # Everything is 1-indexed in this problem
    n = int(input())
    # It stores the index of the person, which our ith indexed (assume it's 1-indexed) person has gifted a gift too
    receiver_index = list(map(int, input().split()))
    # We've to print who gave the gift to the ith receiver starting from 1
    for receiver in range(1, n + 1):
        # Print the correct index of the person who gave our receiver the gift, the answer will be at the position
        # where the receiver value is stored in receiver_index and increment it by 1 so that it becomes 1-indexed
        print(receiver_index.index(receiver) + 1, end=" ")
    print()


if __name__ == "__main__":
    main()
