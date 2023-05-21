from solution import Solution

s = Solution()
INPUT = [
    [1,1,2],
    [0,0,1,1,1,2,2,3,3,4]
]

for ex in INPUT:
    print(s.removeDuplicates(ex))