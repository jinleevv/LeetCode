# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def height(self, root):
    #         if root is None:
    #             return -1
    #         return 1 + max(self.height(root.left), self.height(root.right))

    # def isBalanced(self, root: Optional[TreeNode]) -> bool:
    #     if root is None:
    #         return True
        
    #     if abs(self.height(root.left) - self.height(root.right)) > 1:
    #         return False
        
    #     return self.isBalanced(root.left) and self.isBalanced(root.right)

    def helper(self, root):
        # An empty tree is balanced and has height -1
        if not root:
            return True, -1
        
        # Check subtrees to see if they are balanced. 
        leftIsBalanced, leftHeight = self.helper(root.left)
        if not leftIsBalanced:
            return False, 0
        rightIsBalanced, rightHeight = self.helper(root.right)
        if not rightIsBalanced:
            return False, 0
        
        # If the subtrees are balanced, check if the current tree is balanced
        # using their height
        return (abs(leftHeight - rightHeight) < 2), 1 + max(leftHeight, rightHeight)
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root)[0]