class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: [List[int]]
        """
        self.ans = []
        self.dfs(candidates, target, [])
        return self.ans
    
    def dfs(self, nums, target, path):
        if target < 0:
            return 
        if target == 0:
            self.ans.append(path)
            return 
        for i in range(len(nums)):
            self.dfs(nums[i:], target-nums[i], path+[nums[i]])
