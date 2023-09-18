# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, targetSum, currentSum):
        if not root:
            return 0

        currentSum += root.val
        
        left = self.dfs(root.left, targetSum, currentSum)
        right = self.dfs(root.right, targetSum, currentSum)

        if currentSum == targetSum and not root.left and not root.right:
            return True
        elif left or right:
            return True
        else:
            return False

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.dfs(root, targetSum, 0)
        
