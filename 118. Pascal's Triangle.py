class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        result = numRows and [[1]] or []
        for _ in range(numRows-1):
            result.append([1] + [a + b for a, b in zip(result[-1], result[-1][1:])] + [1])
        return result      
