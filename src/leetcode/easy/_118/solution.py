"""
runtime
    43 ms 78.73%
memory
    16.6 MB 5.75%
"""

from typing import *

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        rows = [[1], [1, 1]]
        
        for i in range(2, numRows):  # init with 2nd row
            rows.append(self.pascal(rows[-1]))
        return rows

    def pascal(self, prevRow: List[int]) -> List[int]:
        """
        given previous row
        apply pascal formula accordingly
        return next row
        """
        # initialize, we'll insert values in middle
        nextRow = [1, 1]
        for i in range(0, len(prevRow) - 1):
            nextRow.insert(-1, prevRow[i] + prevRow[i+1])
        return nextRow