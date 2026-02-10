def main():
    n = int(input())
    heights = list(map(int, input().split()))
    max_h_index, min_h_index = 0, 0
    # We loop from 1 since, we took 0th index height as the max and min height out of all the heights
    # We'll for the max and min height index in the same loop
    for i in range(1, n):
        # If the ith height and max hieght is equal too or greater than
        if heights[i] >= heights[max_h_index]:
            # For the same height store the index which is closest to the first index/front
            if heights[i] == heights[max_h_index]:
                max_h_index = min(max_h_index, i)
            # Else store the current height's index
            else:
                max_h_index = i
        # If the ith height and min height is equal too or less than
        if heights[i] <= heights[min_h_index]:
            # For the same height choose the height closest to last index/end
            if heights[i] == heights[min_h_index]:
                min_h_index = max(min_h_index, i)
            # Else store the current height's index
            else:
                min_h_index = i
    # Answer will be the index position of max height and since it's 0-indexed we don't have to subtract 1 from max height index
    # For min height we have to subtract it from n and in order to find how many indices is it away from last index and we'll
    # subtract 1 from it because n is not number of indices but number of heights.
    answer = max_h_index + n - min_h_index - 1
    # If the max height index is greater than min height index, that means they'll share a common swap.
    if max_h_index > min_h_index:
        answer -= 1
    print(answer)


if __name__ == "__main__":
    main()
