"""Dynamic Programming
Notes:
    problem, what is the longest palindrome, for each poss center indexes (l/r)
    sub-problems, palindrome if left/right letter equal, center palindrome
    the sub-problems use memory of center being palindrome, efficient
O(n^2):
    n, assumptions for center
        n, comparisons to make for assumption
Runtime:
    3096 ms, faster than 25.52% of Python3
Memory Usage:
    13.9 MB, less than 97.61% of Python3
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        longest = ''
        longest_len = 0
        for i in range(0, len(s), +1):
            # odd length
            l, r = i, i
            # while in bounds and is palindrome
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curr = s[l:r+1]
                if len(curr) > longest_len:
                    longest_len = len(curr)
                    longest = curr
                l -= 1
                r += 1
        for i in range(0, len(s), +1):
            # even length
            l, r = i, i + 1
            # while in bounds and is palindrome
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curr = s[l:r+1]
                if len(curr) > longest_len:
                    longest_len = len(curr)
                    longest = curr
                l -= 1
                r += 1
        return longest
