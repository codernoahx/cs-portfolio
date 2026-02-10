class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        # We are basically using DP bottom up approach here. For example, we have to reach 3, How many ways can we reach 3, only one.
        # Now next is 2 how many ways can we reach to 3, only one way. Now 1, how many ways can we reach 3, we know that we can either
        # take one step or two step. At one step we have 2, and at step 2 we have 3. And we know how many ways we can reach to 3.
        # 1 + 1 = 2 ways because we already how many steps we need to from 2 and 3 to reach 3. And now 0, we take one step or two,
        # At one step we have 1 and at step two we have 2, we know how many ways we can reach from 1 and 2. So, 2 + 1 = 3 ways.
        # If we have a bigger number to reach you'll see it's fibonacci numbers. Where we add the n - 1 and n - 2 value to get
        # n. Also since we know the 0th and 1st value, that means we have to iterate n -1 times only. Because 0 is the starting
        # point in the question.
        for _ in range(n - 1):
            # We store one + two in one and swap two with one's value before adding one and two
            one, two = one + two, one
        return one


def main():
    print(Solution().climbStairs(int(input())))


if __name__ == "__main__":
    main()
