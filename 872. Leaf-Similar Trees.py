# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def dfs(node, arr):
            if node:
                if not node.left and not node.right: arr += [node.val]
                dfs(node.left, arr)
                dfs(node.right, arr)
                return arr
        return dfs(root1, []) == dfs(root2, [])
