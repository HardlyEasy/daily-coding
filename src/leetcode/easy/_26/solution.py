"""
runtime
    83 ms 87.76%
memory
    15.6 MB 50.24%
"""

from typing import *

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        stack = [nums[0]]  # duplicates
        for n in nums[1:]:
            if stack[-1] != n:
                stack.append(n)
        nums.clear()
        nums.extend(stack)
        return len(nums)