"""Hashmap, 2-pass (populate hm, pass array + search)
Notes:
    this problem just wants you to get the fastest possible search
    we know what desired number we want, desired = target - num1
    hashmap allows for fast searching, so we'll use that
    constraints of problem are convenient/make things easier also
O(n):
    n, populate hashmap
    n, pass through array
        1, hm search time
Runtime:
    136 ms, faster than 38.94% of Python3
Memory Usage:
    16 MB, less than 8.46% of Python3
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # populate hashmap
        hm = dict()
        for i in range(0, len(nums), +1):
            curr_num = nums[i]
            if curr_num not in hm:
                hm[curr_num] = [i]
            else:
                hm[curr_num].append(i)
        # go through list
        for i in range(0, len(nums), +1):
            curr_num = nums[i]
            desired = target - curr_num
            # same number wanted and 2 numbers exist
            if desired == curr_num and len(hm[desired]) > 1:
                return [i, hm[desired][1]]
            # different number wanted and it exists
            if desired != curr_num and desired in hm:
                return [i, hm[desired][0]]
