class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ind = -1
        for i in s:
            try: ind = t.index(i, ind + 1)
            except: return False
        return True        
