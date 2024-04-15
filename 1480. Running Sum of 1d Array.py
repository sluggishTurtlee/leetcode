class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        l = len(nums)
        nums.reverse()
        value = 0
        result = []

        for i in range(l):
            for j in range(i, l):
                value = value + nums[j]

            result.append(value)
            value = 0
        result.reverse()
        return result
