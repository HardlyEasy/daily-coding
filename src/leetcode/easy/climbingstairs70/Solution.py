"""Hashmap
Notes:
    I probably didn't need a dict?
    Two variables to store 2 previous stairs would've worked too
O(n):
    n, traverse each stair
Runtime:
    46 ms, faster than 26.32% of Python3
Memory Usage:
    13.9 MB, less than 99.72% of Python3
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        return self.climb(n)

    def climb(self, n: int) -> int:
        """Climb and use a dict for quick lookup
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2
        stair_dict = dict()
        stair_dict[1], stair_dict[2] = 1, 2
        for i in range(3, n + 1, +1):
            new = stair_dict[i - 2] + stair_dict[i - 1]
            stair_dict[i] = new
        return stair_dict[n]
