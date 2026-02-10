class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 0, x
        res = 0
        # While low is less than or equal to high
        while low <= high:
            # mid = low + integer division by 2 of difference of high and low
            mid = low + ((high - low) // 2)
            # If mid is the square root we're looking for return mid
            if mid**2 == x:
                return mid
            # Else if square of mid is less than x, mid + 1 becomes our new low and mid becomes our new res
            # The res should be the lowest value closest to the original square root
            elif mid**2 < x:
                low = mid + 1
                res = mid
            # Else if square of mid is greater than x, our new high is mid - 1
            else:
                high = mid - 1
        return res


def main():
    print(Solution().mySqrt(int(input())))


if __name__ == "__main__":
    main()
