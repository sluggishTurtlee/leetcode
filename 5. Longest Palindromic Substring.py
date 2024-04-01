class Solution:
    def expand(self, s: str, t: int, b: int) -> int:
        
        while t >= 0 and b < len(s) and s[t] == s[b]:
            t = t - 1
            b = b + 1
            
        return b - t - 1


    def longestPalindrome(self, s: str) -> str:
        start = 0
        end = 0
        Mlen = 0
        
        for i in range(0, len(s)):
            len1 = self.expand(s, i, i)
            len2 = self.expand(s, i, i+1)
            
            Mlen = max(len1, len2)
            
            if Mlen > end - start + 1:
                start = i - (Mlen - 1) // 2
                end = i + Mlen // 2
        
        return s[start : end+1]
