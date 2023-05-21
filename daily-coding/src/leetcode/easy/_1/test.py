from solution import Solution

s = Solution()

INPUT = [ ([2,7,11,15], 9), ([3,2,4], 6), ([3,3], 6) ]

for ex in INPUT:
    print(s.twoSum(ex[0], ex[1]))