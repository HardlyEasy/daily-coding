"""
time
    36ms 30.7%
memory
    14 MB 9.89%
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack) or len(needle) <= 0:
            return -1
        
        for i in range(0, len(haystack) - len(needle) + 1):
            cut = haystack[i:len(needle) + i]
            if cut == needle:
                return i
        return -1


# double cursor scrapped idea
"""
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        i_hay = 0
        i_needle = 0
        while (i_hay < len(haystack) and i_needle < len(needle)):
            if needle[i_needle] == haystack[i_hay]:
                i_needle += 1
            else:
                i_needle = 0
            i_hay += 1
        if i_needle == len(needle):
            return i_hay - i_needle
        else:
            return -1
"""