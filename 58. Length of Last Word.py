class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        if len(s) == 0:
            return 0

        cnt = 0
        prev = 0
        
        for word in s:
            if cnt > 0:
                prev = cnt
            if word == " ":
                cnt = 0
                continue
            cnt += 1

        if cnt > 0:
            return cnt
        else:
            return prev        
