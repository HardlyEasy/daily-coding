"""
Notes:
    This solution is basically previous two sum problem with a few more steps
    Don't allow any duplicates in i and j position
Time: O(n^2)
    n, pick i
        n, two sum solution
Runtime:
    1180 ms, faster than 54.88% of Python3
Memory Usage:
    18.2 MB, less than 22.68% of Python3
"""


from typing import List


class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        for i, i_val in enumerate(nums):
            # prevent duplicate i
            if i != 0 and nums[i - 1] == i_val:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                three_sum = i_val + nums[j] + nums[k]
                # found triplet
                if three_sum == 0:
                    answer.append([i_val, nums[j], nums[k]])
                    j += 1
                    # prevent duplicate
                    while nums[j - 1] == nums[j] and j < k:
                        j += 1
                elif three_sum > 0:
                    k -= 1
                elif three_sum < 0:
                    j += 1
        return answer
