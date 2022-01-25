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
