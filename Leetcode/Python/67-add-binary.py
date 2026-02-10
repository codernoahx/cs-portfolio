class Solution:
    def addBinary(self, a: str, b: str) -> str:
        la, lb = len(a), len(b)
        res, carry = "", 0
        # We choose the max value between la and lb, and start iterating from 1 to max len, because we'll be accessing values
        # from -1 to -max len
        for i in range(1, max(la, lb) + 1):
            # If the i is less than equal to la (digitA) or lb (digitB) we assign the element at -i index, else 0
            digitA = int(a[-i]) if i <= la else 0
            digitB = int(b[-i]) if i <= lb else 0
            total = digitA + digitB + carry # We sum all of it
            res = str(total % 2) + res # The mod or remainder of total should be added before the res, it'll be either 0 or 1
            carry = total // 2 # The integer division or quotient of total will become the carry it'll be either 0 or 1 
        
        # If any carry was left, meaning the max len will be the size of res but since it has an carry to be included
        # We concatenate 1 at the front, the res size becomes max len + 1
        if carry:
            res = "1" + res
        # We return the res whether the if executes or not
        return res


def main():
    print(Solution().addBinary("11", "1"))


if __name__ == "__main__":
    main()
