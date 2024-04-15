class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        l = len(nums)
        cnt = 0
        result = []

        for i in range(l):
            for j in range(l):
                if nums[i] > nums[j]:
                    cnt += 1
                else: continue
            result.append(cnt)
            cnt = 0

        return result
