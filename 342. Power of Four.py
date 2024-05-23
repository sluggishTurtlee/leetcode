class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 0:
            return False
        i = 1
        while i < n:
            i = i * 4
        return i == n        
