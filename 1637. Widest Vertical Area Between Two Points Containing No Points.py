class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        l = len(points)
        xValue = []
        width = 0
        maxWidth = 0

        for i in range(l):
            xValue.append(points[i][0])
        
        xValue.sort()

        for i in range(l-1):
            width = xValue[i+1] - xValue[i]

            if width >= maxWidth:
                maxWidth = width
            else: continue

        return maxWidth
