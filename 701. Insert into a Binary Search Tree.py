# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root, val):
        if root and root.val > val and not self.insertIntoBST(root.left, val): root.left = TreeNode(val)
        elif root and root.val < val and not self.insertIntoBST(root.right, val): root.right = TreeNode(val)
        return root
