from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        # Keep on iterating till i goes beyond the lower bound
        while i >= 0:
            # If the current digit is below 9, add 1 and return
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # Until the above if doesn't execute we make all the 9's to 0 and keep on waiting for the if statement
            # to execute
            digits[i] = 0
            i -= 1
        # If the above return doesn't execute, that means all the lists elements were 9, which are now 0 and they need a preceding
        # [1] at the front of the list to make the addition correct, and we also increases it's size by 1.
        return [1] + digits


def main():
    print(Solution().plusOne([9, 9, 9]))
    

if __name__ == "__main__":
    main()