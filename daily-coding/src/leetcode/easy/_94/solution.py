from typing import *

"""
runtime
    26 ms 92.9%
memory
    13.9 MB 47.20%
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        curr = root
        l = []

        while True:
            # push up all the way left
            if curr != None:
                stack.append(curr)
                curr = curr.left
            elif stack:
                curr = stack.pop()
                l.append(curr.val)
                curr = curr.right
            else:
                break
        return l

"""
runtime
    31 ms 70.55%
memory
    13.8 MB 94.28%
"""

"""
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l = Solution.recursive(root, [])
        return l

    def recursive(node: TreeNode, l: List[int]) -> List[int]:
        if node == None:
            return l
        Solution.recursive(node.left, l)
        l.append(node.val)
        Solution.recursive(node.right, l)
        return l
"""