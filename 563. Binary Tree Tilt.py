# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def traverse(node):
            if not node: return 0
            left = traverse(node.left)
            right = traverse(node.right)
            res.append(abs(right -left))
            return node.val + left + right
        res = []
        traverse(root)
        return sum(res)
