class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        l = len(words)
        output = []

        for i in range(l):
            if words[i].find(x) > -1:
                output.append(i)
            else:
                continue
        
        return output
