class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans=[]
        l=len(nums)
        for i in range(l):
            ans.append(nums[nums[i]])

        return ans
