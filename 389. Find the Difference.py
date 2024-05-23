class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return next(iter(collections.Counter(t) - collections.Counter(s)))        
