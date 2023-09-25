# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def helper(self, root, p, q, height):
        if not root:
            return root, height
        elif root.left and root.right:
            if (root.left.val == p.val or root.left.val):
                if root.left.val == p.val and root.right.val == q.val:
                    return root, height
                elif root.left.val == q.val and root.right.val == p.val:
                    return root, height
        
        if root.val == p.val or root.val == q.val:
            return root, height

        left, leftVal = self.helper(root.left, p, q, height + 1)
        right, rightVal = self.helper(root.right, p, q, height + 1)

        if left and right:
            return root, -1
        if not left:
            return right, rightVal
        elif not right:
            return left, leftVal
        elif leftVal > rightVal:
            return left, -1
        else:
            return right, -1

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        return self.helper(root, p, q, 0)[0]

        