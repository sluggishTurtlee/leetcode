# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, r: TreeNode, num = 0) -> int:
        if not r: 
            return 0
        num = (num << 1) + r.val
        return (self.sumRootToLeaf(r.left, num) + self.sumRootToLeaf(r.right, num) if r.left or r.right else num) % (10 ** 9 + 7)
