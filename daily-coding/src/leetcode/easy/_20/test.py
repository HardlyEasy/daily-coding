from solution import Solution

s = Solution()

INPUT = ['()', '()[]{}', '(])']

for ex in INPUT:
    print(s.isValid(ex))