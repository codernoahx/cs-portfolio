from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        # l <= r  because we have to include the index when l and r are equal and the only way to check it is when they both
        # are same and we calculate mid. When the target element is greater than our current mid value, we keep on shifting our
        # l pointer to the right by mid + 1. And soon it becomes greater than r or it goes out of bounds if the we're looking
        # for an element greater than the last element, the index value of l becomes n and the index range is n - 1 (n is len(nums)).
        # When the target element is smaller than the mid element value we keep shifting the r pointer to the right by mid - 1.
        # And soon it becomes smaller than l or it goes out of bounds if we're looking for an element smaller than the first element.
        # And l holds the closest lowest bound to that element in this case and in the other case when target is greater than mid,
        # it holds closest greatest bound to that element or the correct index if that element has to be inserted at last.
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return l


def main():
    print(Solution().searchInsert([1, 3, 5, 6], 0))


if __name__ == "__main__":
    main()
