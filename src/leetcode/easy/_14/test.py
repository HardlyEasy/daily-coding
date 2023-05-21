from solution import Solution

INPUT = [
            ['flower', 'flow', 'flight'], 
            ['dog', 'racecar', 'car'],
        ]

s = Solution()

for ex in INPUT:
    print(s.longestCommonPrefix(ex))