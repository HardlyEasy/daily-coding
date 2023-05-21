"""
runtime
    41 ms 52.91%
memory
    13.8 MB 44.2%
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = 4294967295
        mid = (low + high) // 2
        i = 0
        while True:
            # we looked at final possible mid, and no match
            # at this point h m l
            # to round down we should return high
            if low > high:
                return high
            mid = (low + high) // 2
            pow2_mid = mid * mid
            if x > pow2_mid:  # consider right
                low = mid + 1
            elif x < pow2_mid:  # consider left
                high = mid - 1
            elif x == pow2_mid:  # exact match
                return mid
            i+=1
        