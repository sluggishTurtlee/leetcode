class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        dic = set()
        for p in itertools.permutations(nums):
            if p not in dic: 
                dic.add(p)
        return list(dic)        
