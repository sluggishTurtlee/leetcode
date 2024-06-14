# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [0]
        def traverse(node):
            if not node: return 0
            left, right = traverse(node.left), traverse(node.right)
            res[0] = max(left+right, res[0])
            return 1+ max(left, right)
        traverse(root)
        return res[0]     
