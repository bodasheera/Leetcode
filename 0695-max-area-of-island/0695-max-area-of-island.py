class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        

        n = len(grid)
        m = len(grid[0])


        def sink(r, c):

            # base case - out of bound
            if r < 0 or r > n - 1 or c < 0 or c > m -1 :
                return 0

            # base case - water
            if grid[r][c] == 0:
                return 0

            # induction - sink the island
            grid[r][c] = 0

            # hypothesis
            return 1 + sink(r-1, c) + sink(r+1, c) +  sink(r, c-1) + sink(r, c+1)

           

        res = 0

        for i in range(n):
            for j in range(m):

                if grid[i][j] == 1:
                    
                    res = max(res, sink(i, j))

        return res
