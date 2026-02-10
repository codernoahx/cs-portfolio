class Solution(object):
    def twoSum(self, nums, target):
        # Hashmap to store index of numbers from nums list
        num_to_index = {}  # numbers -> index

        # Iterating over the nums array with indices and elements from the nums list.
        for i, num in enumerate(nums):
            # If a + b = target, then b = target - a. That's why we're finding the difference between
            # the current element and the target to see if the difference exists in the hashmap. Since
            # there exists only one pair of elements whose sum is equal to the target. Hashmap helps us
            # in exiting the loop prematurely as soon as we find the difference if we have hashed it
            # previously, if not we hash the number. It's like a = target - b or b = target - a.
            # Eventually we'll find the number which matches the difference. This saves us the
            # trouble of hashing all the values previously. We're hashing while iterating, so even
            # if we miss a we'll eventually get to it later through b. This saves us space and time
            # by making sure we iterate over the nums list only once.
            diff = target - num
            if diff in num_to_index:
                return [num_to_index[diff], i]
            num_to_index[num] = i
        return []


obj = Solution()
result = obj.twoSum([2, 7, 11, 15], 9)
print(result)
