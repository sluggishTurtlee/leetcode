class Solution:
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        from collections import Counter
        def traverse(node):
            if node: dic[node.val]+=1; traverse(node.left); traverse(node.right)
        dic = collections.Counter()
        traverse(root)
        mx=max(dic.values(),default=0)
        return [k for k,v in dic.items() if v==mx]
