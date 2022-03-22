"""
Notes:
    None
Time Complexity: O(n)
    Swap operation must be done on every cell of matrix
Runtime:
    54 ms, faster than 42.37% of Python3
Memory Usage:
    14 MB, less than 41.79% of Python3
"""

import math
from typing import *


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """Rotate an entire matrix 90 degrees clockwise, in place (adjust
        matrix as is)
        """
        n = len(matrix)
        y1_x2_list = list(range(0, len(matrix)))
        # Old y index maps to new x index
        y1_x2_list.reverse()
        stop_y = math.ceil(n / 2)
        low_limit_x, up_limit_x = 0, n - 1
        y = 0
        while y != stop_y:
            self.swap_square(matrix, low_limit_x, up_limit_x, y, y1_x2_list)
            low_limit_x += 1
            up_limit_x -= 1
            y += 1
        print(matrix)

    def swap_square(self, matrix: List[List[int]], low_limit_x: int,
                    up_limit_x: int, y: int, y1_x2_list: List[int]):
        """Swap a outer square section of matrix with inside hollowed out
        """
        curr_x = low_limit_x
        while curr_x != up_limit_x:
            self.four_swap(matrix, curr_x, y, y1_x2_list)
            curr_x += 1

    def four_swap(self, matrix: List[List[int]],
                  x1: int, y1: int, y1_x2_list: List[int]):
        """Given a starting position, swap 1st val to 2nd position,
        2nd val to 3rd position, and swaps 3rd val with 4th position
        """
        count = 0
        queue = [matrix[y1][x1]]
        while count < 4:
            x2, y2 = y1_x2_list[y1], x1
            # Remember displaced value
            queue.append(matrix[y2][x2])
            # Assign new value, displacing a value
            matrix[y2][x2] = queue.pop(0)
            x1, y1 = x2, y2
            count += 1
