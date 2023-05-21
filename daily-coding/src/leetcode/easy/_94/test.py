from solution import Solution, TreeNode

s = Solution()

ex1 = TreeNode(1)
ex1.left = None
ex1.right = TreeNode(2)
ex1.right.left = TreeNode(3)

ex2 = None

ex3 = TreeNode(1)

INPUT = [ex1, ex2, ex3]

for ex in INPUT:
    print(s.inorderTraversal(ex))