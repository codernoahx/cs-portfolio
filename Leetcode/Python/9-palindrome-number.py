class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers aren't palindrome because of the - sign
        if x < 0:
            return False

        div = 1
        # Keeps on looping until we get div and x having the same number of places
        while x >= div * 10:
            div *= 10

        while x:
            # Gets us the last digit
            r = x % 10
            # Gets us the first digit
            l = x // div
            # If the digits aren't same we return False
            if l != r:
                return False
            # We trim the first digit from x
            x %= div
            # We trim the last digit from x
            x //= 10

            # or x = (x % div) // 10
            # We trim the last two zero's from div, to match the number of places with x
            div //= 100
        return True


obj = Solution()
result = obj.isPalindrome(int(input()))
print(result)
