class Solution:
    def isValid(self, s: str) -> bool:
        lst, L, R = [], ("(", "[", "{"), (")", "]", "}") 

        for char in s:
            if char in L: 
                lst.append(char)
            elif not lst or L.index(lst.pop()) != R.index(char): 
                return False

        return not lst 
