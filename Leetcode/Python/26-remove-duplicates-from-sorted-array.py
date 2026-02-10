from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # We initialize l and r at 1 because the first element in the list is at the correct position
        l = 1
        for r in range(1, len(nums)):
            # We look for the value which is different from the previous value
            if nums[r] != nums[r - 1]:
                # We assign that value to the place our l pointer is pointing too
                nums[l] = nums[r]
                # Increment the l pointer by 1
                l += 1
        # We return l because we've to return unique k elements and since we keep our l pointer 1 index ahead so that we can
        # assign the next non-duplicate value to that place. But if we never found that value for the place where l is pointing
        # We know it's ahead by 1 but it also tells us how far we have removed the duplicates from the list.
        return l


def main():
    obj = Solution()
    result = obj.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
    print(result)


if __name__ == "__main__":
    main()
