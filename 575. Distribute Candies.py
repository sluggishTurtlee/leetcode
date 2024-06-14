class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        return len(set(candyType)) if len(set(candyType))<=len(candyType)//2 else len(candyType)//2        
