# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def helper(self, root, p, q, height):
    #     if not root:
    #         return root, height
    #     elif root.left and root.right:
    #         if (root.left.val == p.val or root.left.val):
    #             if root.left.val == p.val and root.right.val == q.val:
    #                 return root, height
    #             elif root.left.val == q.val and root.right.val == p.val:
    #                 return root, height
        
    #     if root.val == p.val or root.val == q.val:
    #         return root, height

    #     left, leftVal = self.helper(root.left, p, q, height + 1)
    #     right, rightVal = self.helper(root.right, p, q, height + 1)

    #     if left and right:
    #         return root, -1
    #     if not left:
    #         return right, rightVal
    #     elif not right:
    #         return left, leftVal
    #     elif leftVal > rightVal:
    #         return left, -1
    #     else:
    #         return right, -1
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # return self.helper(root, p, q, 0)[0]

        def recurse_tree(current_node):
            # If reached the end of a branch, return False.
            if not current_node:
                return False

            # Left Recursion
            left = recurse_tree(current_node.left)

            # Right Recursion
            right = recurse_tree(current_node.right)

            # If the current node is one of p or q
            mid = current_node == p or current_node == q

            # If any two of the three flags left, right or mid become True.
            if mid + left + right >= 2:
                self.ans = current_node

            # Return True if either of the three bool values is True.
            return mid or left or right
            
        recurse_tree(root)
        return self.ans