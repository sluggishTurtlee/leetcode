class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        a = n - len([nums.pop(i) for i in range(n -1, 0, -1) if nums[i] == nums[i - 1]])

        return a
