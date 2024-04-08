class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l = len(nums)
        new = []
        y = l//2 

        for i in range(l//2):
            new.append(nums[i])
            new.append(nums[y])
            y += 1

        return new
