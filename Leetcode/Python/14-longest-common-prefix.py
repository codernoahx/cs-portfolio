from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # The way we solve this is we choose the first string from the list and iterate through every single char in it. Next we
        # We create another loop which iterate over every single string from the list. Now what we do is we pick the current
        # string we're iterating over in the inner loop and compare it's char with our string 0's char. The outer loop starts
        # with value 0 using that we access the first element of string 0 and we can access the 0th index value of the string
        # in the inner loop. Now what we do is we compare every single string 0th index value with string 0's 0th index value
        # and by any chance if thevalue of any string in the string doesn't match 0th place of our string 0 we return empty
        # or maybe there is an empty string we return empty string. And then in the next iteration of our outer loop we compare
        # string (string[:0] => "") the value's of string 0 and every single string's 1st index. If the value don't match we
        # retun prefix excluding 1st position or if len is 1 of the compared string then we return. We keep on doing i until
        # either the length of compared string goes out of bounds or the character doesn't match of any compared string in
        # that iteration, and thus we return. If none of these cases ever evaluate to True then, we execute the return statement
        # at the bottom of the function. If this return statement executes this means all the strings in the list are
        # same/duplicates, since they're same they've the same length. We cansafely return the first string or maybe
        # this list has only one string.

        # Iterate through every single char of the string at 0th index from the list of strings.
        for i in range(len(strs[0])):
            # Now from the list of strings we'll compare every single string's ith position with the ith position of our
            # 0th index string.
            for string in strs:
                # If the current string doesn't have ith position, i.e., it is smaller than our string 0, we can return prefix
                # excluding ith place OR if the char at ith index of our current string doesn't match the ith char value of our
                # string 0, return the prefix excluding the ith place
                if i == len(string) or string[i] != strs[0][i]:
                    return string[:i]
        return strs[0]


obj = Solution()
result = obj.longestCommonPrefix(["flower", "flow", "flight"])
print(result)
