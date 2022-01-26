from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for li in range(0, len(nums) - 1, +1):
            for ri in range(li + 1, len(nums), +1):
                if (nums[li] + nums[ri]) == target:
                    return [li, ri]