"""Dynamic Programming, Kadane's Algorithm
Notes:
    problem, largest contiguous sum, at each index
    sub-problem, largest sum is max(prev_max, prev_max + curr_num)
    the sub-problems use memory of previous maximum, efficient
O(n):
    n, find local_max at each index and set new global max if possible
Runtime:
    954 ms, faster than 40.87% of Python3
Memory Usage:
    28.4 MB, less than 73.64% of Python3
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """Kadane's Algorithm used
        Finds largest sum of contiguous subarray globally
        """
        local_max = 0
        global_max = float('-inf')  # smaller than any int
        for i in range(0, len(nums), +1):
            local_max = max(nums[i], nums[i] + local_max)
            if local_max > global_max:
                global_max = local_max
        return global_max
