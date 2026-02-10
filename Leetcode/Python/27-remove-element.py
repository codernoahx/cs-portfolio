from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # We set l and r to 0 because we need to ensure elements from 0 to k doesn't contain val
        # l is incremented only when we find a value which != val
        l = 0
        for r in range(len(nums)):
            # We have to skip every index when element at index r == val
            # If nums at index r is not equal to val
            if nums[r] != val:
                # We set the value stored at index r at index l
                nums[l] = nums[r]
                l += 1  # And then increment l by 1

        # We return l since it includes how many times we shifted our l pointer and since it's 0 indexed we kept our pointer
        # 1 value ahead, which gives us the correct unique k elements
        return l


def main():
    result = Solution().removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)
    print(result)


if __name__ == "__main__":
    main()
