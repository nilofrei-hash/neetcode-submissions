class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        output = 0
        n = len(mat)

        for i in range(n):
            output += mat[i][i]
            output += mat[i][n - 1 - i]

            if i == n - 1 - i:
                output -= mat[i][i]

        return output

        