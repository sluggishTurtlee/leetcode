class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        wordLength = []
        l = len(sentences)

        for i in range(l):
            wordLength.append(sentences[i].count(' ') + 1)

        return wordLength[wordLength.index(max(wordLength))]
