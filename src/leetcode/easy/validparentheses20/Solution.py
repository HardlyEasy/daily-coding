"""Stack solution
Notes:
    Key to this problem is to use stack
Time Complexity: O(n)
    all operations under for loop take constant time
Space Complexity:

Runtime:
    41 ms, faster than 62.35% of Python3
Memory Usage:
    14.1 MB, less than 13.90% of Python3
"""


class Solution:
    def isValid(self, s: str) -> bool:
        """Returns true if legal arrangement of brackets
        """
        left_symbols = []
        for i in range(0, len(s), +1):
            # Check for left symbol
            if self.isLeft(s[i]):
                # add to left list (acts like stack)
                left_symbols.append(s[i])
            # Ensured right symbol by constraints from here on
            # Encountered right symbol without any left in stack
            elif len(left_symbols) == 0:
                return False
            # Popped left symbol doesn't match right symbol
            elif not self.isClosing(left_symbols.pop(), s[i]):
                return False
        if len(left_symbols) > 0:
            return False
        return True

    def isLeft(self, c: str):
        """Returns true if character is left type of bracket
        """
        if c == '(' or c == '[' or c == '{':
            return True

    def isClosing(self, left: str, right: str):
        """Returns true is left and right are matching pairs
        """
        if left == '(' and right == ')':
            return True
        elif left == '[' and right == ']':
            return True
        elif left == '{' and right == '}':
            return True
        else:
            return False
