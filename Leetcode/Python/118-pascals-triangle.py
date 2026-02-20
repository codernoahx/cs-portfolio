from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        # We created the first row, that's why -1
        for _ in range(numRows - 1):
            # Adding 0 at both ends in temp list, so that we can get 1 at both ends for the next row easily.
            # We'll calculate the sum of two adjacent elements and append it in the new list.
            temp = [0] + res[-1] + [0]
            # To temporarily store the newly generated list
            row = []
            # Loop till the len of previous row + 1, since the new row will have 1 more element
            for i in range(len(res[-1]) + 1):  # range(len(temp) - 1):
                # Append the sum of adjacent elements
                row.append(temp[i] + temp[i + 1])
            # Append the newly generated list in res list
            res.append(row)
        return res
