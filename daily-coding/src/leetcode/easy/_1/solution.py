from typing import *

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # populate dict, key=n, value=[i0,i1,i2...]
        d = dict()
        for i in range(0, len(nums)):
            n = nums[i]
            if n not in d:
                d[n] = [i]
            else:
                d[n].append(i)
        # 
        for first in nums:
            second = target - first
            if second in d:
                # match: identical first second
                if first == second:
                    if len(d[first]) > 1:
                        return d[first][:2]
                # match: different first second
                else:
                    return [d[first][0], d[second][0]]