class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        l = len(nums)
        result = 0

        for i in range(l):
            if k == bin(i).count('1'):
                result = result + nums[i]
            else: continue

        return result
