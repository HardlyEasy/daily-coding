from leetcode.easy.longestcommonprefix14.Solution import Solution

s = Solution()
# print(s.is_common_prefix(['flower', 'flow', 'flight'], 2))
# print(s.is_common_prefix(['flower', 'flow', 'flight'], 3))

print(s.longestCommonPrefix(['flower', 'flow', 'flight']))
print(s.longestCommonPrefix(['dog', 'racecar', 'car']))
print(s.longestCommonPrefix(['ab', 'a']))
print(s.longestCommonPrefix(['z', 'z']))
print(s.longestCommonPrefix(['flower', 'flower', 'flower']))