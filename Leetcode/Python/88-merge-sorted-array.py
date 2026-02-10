from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # We'll merge the list from the last elements
        last = m + n - 1
        i, j = m - 1, n - 1
        # If there are no elements in nums2 to add in nums1 that means the rest of the elements in nums1 are sorted, since the
        # the size of nums1 is m + n, so there won't be element left if j elements are added in nums1
        while j >= 0:
            # If there are still elements left in nums1 to be appended at the back and which are greater than the nums2 element
            if i >= 0 and nums1[i] > nums2[j]:
                # Store it at the last
                nums1[last] = nums1[i]
                # Decrement the nums1 pointer since that element is at it's correct place
                i -= 1
            # Else if nums2 element is larger
            else:
                # Store the element at the last of the list
                nums1[last] = nums2[j]
                # Since that element is stored at the correct place, decrement the nums2 pointer
                j -= 1
            # And at the end of each iteration, decrement the last pointer by - 1 since the position last was pointing has the
            # correct element in place
            last -= 1


def main():
    nums1 = []
    nums2 = []
    Solution().merge(nums1, nums2)
    print(nums1)


if __name__ == "__main__":
    main()
