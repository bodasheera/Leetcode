class Solution:
    def convert(self, s: str, numRows: int) -> str:

        size = len(s)

        if size <= numRows or numRows == 1:
            return s


        x, _ = divmod(size, numRows)
        y = (numRows - 2) * (x-1)
        numCols = size
        matrix = [[''] * numCols for _ in range(numRows)]

        r = 0
        c = 0

        i = 0
        skipCols = numRows - 2 + 1

        over = False

        for col in range(0, numCols, skipCols):
            for row in range(numRows):

                if i < size:
                    matrix[row][col] = s[i]
                else:
                    over = True
                    break

                i += 1

            if over is True:
                break

            temp_row = numRows - 2
            total_cols = numRows - 2
            temp_col = col + 1

            while total_cols != 0 and i < size:
                matrix[temp_row][temp_col] = s[i]
                i += 1
                temp_row -= 1
                temp_col += 1
                total_cols -= 1

            if i >= size:
                over = True            

            if over is True:
                break

        res = ""

        for r in range(numRows):
            for c in range(numCols):
                if matrix[r][c] != '':
                    res += matrix[r][c]

        return res