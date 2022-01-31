"""Hashmap
Notes:
    not much going on here
    hashmap for fast lookup and O(n) to iterate through
    weirdness with making sure left/right index are in right place
    this weirdness could prob be improved on, but whatever
O(n):
    n, advance left/right index
        1, check single/double dicts
Runtime:
    52 ms, faster than 64.60% of Python3
Memory Usage:
    13.9 MB, less than 99.89% of Python3
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        single_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                       'C': 100, 'D': 500, 'M': 1000}
        double_dict = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
                       'CD': 400, 'CM': 900}
        if len(s) == 1:  # Simplest case
            return single_dict[s]
        total = 0
        li, ri = 0, 1  # left index, right index
        while li < len(s):
            if ri < len(s):  # Guard against out of bounds
                double = s[li:ri+1]
                if double in double_dict:  # Check double dict
                    total += double_dict[double]
                    li += 2
                    ri += 2
                    continue
            single = s[li]
            if single in single_dict:  # Check single dict
                total += single_dict[single]
                li += 1
                ri += 1
        return total
