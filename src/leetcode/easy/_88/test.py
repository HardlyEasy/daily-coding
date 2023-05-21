from solution import Solution

s = Solution()

INPUT = [
    ([1,2,3,0,0,0], 3, [2,5,6], 3),
    #([1], 1, [], 0),
    #([0], 0, [1], 1),
    #([4,5,6,0,0,0], 3, [1,2,3], 3)
]

for ex in INPUT:
    s.merge(ex[0], ex[1], ex[2], ex[3])
    #print(ex[0], ex[2])