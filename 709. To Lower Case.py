class Solution(object):
    def toLowerCase(self, str):
        """
        :type s: str
        :rtype: str
        """
        return "".join(chr(ord(c) + 32) if 65 <= ord(c) <= 90 else c for c in str)        
