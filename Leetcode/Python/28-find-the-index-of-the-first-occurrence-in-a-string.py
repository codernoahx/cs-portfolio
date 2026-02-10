class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Finds the first occurence of the sub string, and returns the index of the start char of that sub string
        # And if that sub string doesn't exist, we return -1
        return haystack.find(needle)


def main():
    print(Solution().strStr("leetcode", "leeto"))


if __name__ == "__main__":
    main()
