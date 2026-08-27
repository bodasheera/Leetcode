class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        
        n = len(matrix)
        res = []
        
        for i in range(n):
            ct = 0
            for j in range(n):
                if matrix[i][j] == 1:
                    ct += 1
            res.append(ct)

        return res