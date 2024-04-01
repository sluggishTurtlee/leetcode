class Solution:
    def convert(self, s: str, numRows: int) -> str:
        p = 0
        q = 0
        zigzag = ''
        Dic = dict()

        
        for i in range(0, numRows):
            Dic[i] = []
        
        for j in range(0, len(s)):
            Dic[q] += s[j]
            
            if p == 0:
                q += 1
            else:
                q -= 1
            
            if q == numRows:
                if numRows >= 3:
                    q -= 2
                    p = 1
                else:
                    q = 0
            
            if q == 0:
                p = 0
        
        for k in range(0, len(Dic)):
            for l in range(0, len(Dic[k])):
                zigzag += Dic[k][l]
        
        return zigzag
