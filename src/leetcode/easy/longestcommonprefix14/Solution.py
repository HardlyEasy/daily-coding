"""Binary Search
Notes:
    bit confusing on indexes and where to stop/where midpt is (even/odd)
    time complexity O(log n) is probs roughly right, but this might be
    a little diff than a usual binary search b/c of its string, not int array
O(log n): (? checking till min str length changes this ?)
    log(base2)n, number of splitting operations
Runtime:
    31 ms, faster than 87.98% of Python3
Memory Usage:
    13.9 MB, less than 99.95% of Python3
"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # optimize a bit (only check till minimum str length)
        min_str = min(strs, key=len)
        li, hi = 0, len(min_str) - 1  # low index , high index

        while li <= hi:
            mi = (li + hi) // 2  # middle index
            # if substr up to and including midpoint
            if self.is_common_prefix(strs, mi):
                li = mi + 1  # search after midpoint in next pass
            # else not substr up to and including midpoint
            else:
                hi = mi - 1  # search before midpoint in next pass
        return strs[0][0:((li + hi)//2)+1]

    def is_common_prefix(self, strs: List[str], mi) -> bool:
        """Checks if substring is prefix of all strings in string array
        """
        for i in range(1, len(strs)):
            if strs[i][0:mi+1] != strs[0][0:mi+1]:
                return False
        return True
