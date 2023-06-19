"""
runtime
    50 ms 32%
memory
    16.3 MB 63%
"""

from typing import *

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        prevRow = [1, 1]
        for i in range(2, rowIndex + 1):
            prevRow = self.pascal(prevRow)
        return prevRow

    def pascal(self, prevRow: List[int]) -> List[int]:
        nextRow = [1, 1]
        for i in range(0, len(prevRow) - 1):
            nextRow.insert(-1, prevRow[i] + prevRow[i + 1])
        return nextRow