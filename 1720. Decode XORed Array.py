class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        decList = [first]

        for encElement in encoded:
            decList.append(decList[-1] ^ encElement)

        return decList
