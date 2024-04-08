class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        l=len(nums)
        j=0
        good=0

        for i in range(l):
            for j in range(i+1, l):
                if nums[i]==nums[j]:
                    good=good+1
                else: continue
        
        return good
