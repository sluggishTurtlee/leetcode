class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        return all(matrix[i][j] == matrix[i - 1][j - 1] for i in range(1, len(matrix)) for j in range(1, len(matrix[0])))
