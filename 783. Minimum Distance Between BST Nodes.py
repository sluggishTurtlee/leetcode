# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node):
            if not node: return float("inf"), float("inf"), -float("inf")
            l, lMn, lMx = dfs(node.left)
            r, rMn, rMx = dfs(node.right)
            return min(l, node.val - lMx, r, rMn - node.val), min(lMn, node.val), max(rMx, node.val)
        return dfs(root)[0]        
