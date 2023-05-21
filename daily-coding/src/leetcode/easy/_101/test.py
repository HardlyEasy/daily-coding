from solution import Solution, TreeNode

s = Solution()
tn1 = TreeNode(1)
tn1.left = TreeNode(2)
tn1.left.left = TreeNode(3)
tn1.left.right = TreeNode(4)
tn1.right = TreeNode(2)
tn1.right.left = TreeNode(4)
tn1.right.right = TreeNode(3)

print(s.isSymmetric(tn1))
