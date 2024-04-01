class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        Mlen = 0
        i = 0
        Dict = dict()
        
        for j in range(0, len(s)):
            if Dict.get(s[j]) != None:
                i = max(Dict[s[j]], i)
            
            Dict[s[j]] = j+1
            Mlen = max(j-i+1, Mlen)
        
        return Mlen
