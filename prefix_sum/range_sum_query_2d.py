class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        rows = len(matrix)
        cols = len(matrix[0])

        self.prefix_sum = [[0] * (cols + 1) for c in range(rows + 1)]
        for r in range(rows):
            prefix = 0
            for c in range(cols):
                prefix += matrix[r][c]
                above = self.prefix_sum[r][c + 1]
                self.prefix_sum[r + 1][c + 1] = prefix + above
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        row1, col1 = row1 + 1, col1 + 1
        row2, col2 = row2 + 1, col2 + 1
        region_sum = 0

        bottom_right = self.prefix_sum[row2][col2]
        above = self.prefix_sum[row1 - 1][col2]
        left = self.prefix_sum[row2][col1 - 1]
        top_left = self.prefix_sum[row1 - 1][col1 - 1]
        
        return bottom_right - above - left + top_left


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)