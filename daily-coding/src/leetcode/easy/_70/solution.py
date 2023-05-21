"""
runtime
    27 ms 86.60%
memory
    13.8 MB 93.52%
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        one_below = 2  # number of ways to get 1 step below curr
        two_below = 1 
        for curr in range(3, n + 1):
            temp_two_below = two_below
            two_below = one_below
            one_below = one_below + temp_two_below
        return one_below

"""
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)
""" 