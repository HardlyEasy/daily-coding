from solution import Solution

s = Solution()
INPUT = [
    ('sadbutsad', 'sad'),
    ('leetcode', 'leeto'),
    ('sasadsa', 'sad')
]


for ex in INPUT:
    print(s.strStr(ex[0], ex[1]))