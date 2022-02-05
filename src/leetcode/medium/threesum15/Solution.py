"""

Runtime:
    900 ms, faster than 74.81% of Python3
Memory Usage:
    21.9 MB, less than 5.32% of Python3
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        hm = dict()
        sol_set = set()
        answer = []
        # populate hashmap
        for i in range(0, len(nums), +1):
            if nums[i] not in hm:
                hm[nums[i]] = 1
            else:
                hm[nums[i]] += 1
        keys = list(hm.keys())
        # cover triplet special case
        if 0 in hm and hm[0] >= 3:
            answer.append([0, 0, 0])
        # pick i
        for i in range(0, len(keys), +1):
            i_val = keys[i]
            # find k (covers any duplicates case)
            if hm[i_val] >= 2:
                k_val = -i_val * 2
                if k_val in hm and k_val != 0:
                    sol_set.add(frozenset([i_val, i_val, k_val]))
            # pick j
            for j in range(i + 1, len(keys), +1):
                j_val = keys[j]
                # find k (covers non duplicates case)
                k_val = -i_val - j_val
                if k_val in hm and i_val != j_val and i_val != k_val and \
                        j_val != k_val:
                    sol_set.add(frozenset([i_val, j_val, k_val]))
        answer = self.tidy_set(sol_set, answer)
        return answer

    def tidy_set(self, sol_set, answer):
        for triplet in sol_set:
            triplet = list(triplet)
            if len(triplet) == 1:
                triplet.extend([0, 0])
                answer.append(triplet)
            elif len(triplet) == 2:
                if triplet[0] + triplet[0] + triplet[1] == 0:
                    triplet.append(triplet[0])
                    answer.append(triplet)
                elif triplet[0] + triplet[1] + triplet[1] == 0:
                    triplet.append(triplet[1])
                    answer.append(triplet)
            else:
                answer.append(triplet)
        return answer
