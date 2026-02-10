class Solution:
    def isValid(self, s: str) -> bool:
        # Maps closing brackets to open brackets
        close_to_open = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        stack = []
        # Iterate over every single character in the string
        for char in s:
            # If it is a closing bracket
            if char in close_to_open:
                # We make sure the stack isn't empty if it is empty that means we have a closing bracket before an opening bracket
                # If the element on top of the stack or the element at the end of the list has the same opening bracket as the
                # closing bracket's opening bracket then we pop that opening bracket since it was correctly closed.
                if stack and stack[-1] == close_to_open[char]:
                    stack.pop()
                # Else if the stack is empty and the opening brackets don't match we return False
                else:
                    return False
            # Else append/push it to the stack
            else:
                stack.append(char)
        # If the stack isn't empty that means an unclosed bracket is left in the stack in that case we return False
        # If the stack in empty we return True
        # return len(stack) == 0
        return True if not stack else False


def main():
    obj = Solution()
    result = obj.isValid(input())
    print(result)


if __name__ == "__main__":
    main()
