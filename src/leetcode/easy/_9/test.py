from solution import Solution, Solution2

s = Solution()
s2 = Solution2()
INPUT = [121, -121, 10]

print('=====solution1=====')
for ex in INPUT:
    print(s.isPalindrome(ex))

print('=====solution2=====')
for ex in INPUT:
    print(s2.isPalindrome(ex))