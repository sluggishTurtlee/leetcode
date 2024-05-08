class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        l = len(digits)
        dec = 0

        for i in range(l):
            dec += digits[i] * 10**i
        
        new = list(str(dec + 1))

        return map(int, new)
