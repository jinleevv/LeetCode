# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = []
        result = []

        if root is None:
            return []

        queue.append(root)

        while queue:
            length = len(queue)
            level = []

            for i in range(length):
                element = queue.pop(0)
                level.append(element.val)
                
                if element.left:
                    queue.append(element.left)
                if element.right:
                    queue.append(element.right)
                    
            result.append(level)
            level = []

        return result
            