class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        l = len(nums)
        result = 0

        for i in range(l-1):
            for j in range(i+1, l):
                if nums[i] + nums[j] < target:
                    result += 1
                else: continue
        
        return result
