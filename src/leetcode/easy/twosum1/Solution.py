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
