from typing import *

"""
runtime
    41 ms 13.37%
memory
    13.8 MB 46.38%
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) -1, -1, -1):
            added = digits[i] + 1
            if added == 10:
                digits[i] = 0
                if i == 0:  # no next
                    digits.insert(0, 1)
            elif 1 <= added <= 9:
                digits[i] += 1
                break
        return digits

"""
runtime
    31 ms 79.72%
memory
    13.7 MB 94.15%
"""

"""
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''
        for d in digits:
            s += str(d)
        added_s = str(int(s) + 1)
        
        plus_one = []
        for c in added_s:
            plus_one.append(int(c))
        return plus_one
"""