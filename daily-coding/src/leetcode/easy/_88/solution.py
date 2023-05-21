from typing import *

"""
runtime
    37 ms 73.2%
memory
    13.9 MB 74.30%
"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], 
            n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        sliced1 = nums1[:m]
        nums1.clear()
        nums1.extend(sliced1)
        nums1.extend(nums2)
        nums1.sort()