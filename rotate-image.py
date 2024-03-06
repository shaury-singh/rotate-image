class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for rows in range(len(matrix)):
            for cols in range(len(matrix[rows])):
                temp = matrix[rows][cols]
                matrix[rows][cols] = matrix[cols][rows]
                matrix[cols][rows] = temp
        for rows in matrix:
            rows.reverse()
