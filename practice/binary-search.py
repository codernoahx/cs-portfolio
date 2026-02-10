def main():
    print(
        binary_search(
            [1, 2, 4, 7, 8, 23, 27, 31, 33, 43, 56, 65, 71, 83, 85, 98, 105, 123], 43
        )
    )


def binary_search(nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
        m = (l + r) // 2
        if target == nums[m]:
            return True
        elif nums[m] < target:
            l = m + 1
        else:
            r = m - 1
    return False


if __name__ == "__main__":
    main()
