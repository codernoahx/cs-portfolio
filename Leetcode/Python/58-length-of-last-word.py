class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length, i = 0, len(s) - 1
        # Move pointer to the first non-space char from the end of the string
        while s[i] == " ":
            i -= 1
        # Keep on iterating until i goes out of bounds or the s[index] evaluates to a space
        while s[i] != " " and i >= 0:
            length += 1
            i -= 1
        return length


def main():
    print(Solution().lengthOfLastWord(input()))


if __name__ == "__main__":
    main()
