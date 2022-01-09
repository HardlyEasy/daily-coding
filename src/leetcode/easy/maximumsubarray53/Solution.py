

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
