from typing import *

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # sort by length
        strs = sorted(strs, key=len)
        # pick one of longest strings to compare other strings to
        compare = strs[-1]
        strs = strs[:-1]
    
        prefix = ''
        for i in range(1, len(compare) + 1):
            compare_prefix = compare[:i]
            for s in strs:
                if s.find(compare_prefix) != 0:
                    return prefix
            prefix = compare_prefix
        return prefix