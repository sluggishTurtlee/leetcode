class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        MaxCandies = max(candies)
        answers = []
        for i in candies:
            if i + extraCandies >= MaxCandies:
                answers.append(True)
            else:
                answers.append(False)
        return answers
