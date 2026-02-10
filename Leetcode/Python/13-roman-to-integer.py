class Solution:
    def romanToInt(self, s: str) -> int:
        # Hasmap of roman numeral symbols to int
        romToInt = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res = 0
        length = len(s)

        for i in range(length):
            # If the current value has a next value within bounds, then check if the current value is smaller than the next value
            if i + 1 < length and romToInt[s[i]] < romToInt[s[i + 1]]:
                res -= romToInt[s[i]] # If it is subtract it from res
            else:
                res += romToInt[s[i]] # else add it to res
        return res


obj = Solution()
print(obj.romanToInt(input()))
