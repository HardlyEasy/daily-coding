class Solution:
    def isValid(self, s: str) -> bool:
        stack_l = []  # use list as stack
        dict_l_r = {'(': ')', '[': ']', '{': '}'}

        for ch in s:
            if ch in dict_l_r:  # left symbol
                stack_l.append(ch)
            elif ch in dict_l_r.values():  # right symbol
                if len(stack_l) == 0:  # no left to match
                    return False
                elif ch != dict_l_r[stack_l.pop()]:  # mismatch
                    return False
        if len(stack_l) != 0:  # extra left means false
            return False
        return True