"""Exploit Sorted
Notes:
    Left start at index 0 (move to get higher sum)
    Right start at end (move to get lower sum)
    We take advantage of sorted property
    Hard to describe, elimination and lookup are both related to sorted
Time: O(n)
    n, adjust li and ri
Runtime:
    148 ms, faster than 8.13% of Python3
Memory Usage:
    15 MB, less than 30.70% of Python3
"""


from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        li, ri = 0, len(numbers) - 1
        # Constraints guarantee a solution
        while True:
            summed = numbers[li] + numbers[ri]
            if summed < target:
                li += 1
            elif summed > target:
                ri -= 1
            elif summed == target:
                return [li+1, ri+1]
