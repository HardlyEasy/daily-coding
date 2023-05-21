import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:  # all negatives are not palindromes
            return False
        s = str(x)
        low, high = 0, len(s) - 1
        while low <= high:
            if s[low] != s[high]:
                return False
            low += 1
            high -= 1
        return True

# Could you solve it without converting the integer to a string?
class Solution2:
    def isPalindrome(self, x: int) -> bool:
        # no negatives can be palindromes
        if x < 0:  
            return False
        # no positives can have zero in ones digit
        elif x > 0:
            if x % 10 == 0:
                return False
        # zero always palindrome
        elif x == 0:
            return True

        x_chop = x  # temp copy
        reverse = 0

        while x_chop > 0:
            # chops off right digit from n
            right = x_chop % 10
            x_chop = math.floor(x_chop * .10)
            # adds right digit to reverse
            reverse = reverse * 10
            reverse += right
        if reverse == x:
            return True
        return False