class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        rows = {}
        for row in grid:
            row_string = str(row)
            if row_string not in rows:
                rows[row_string] = 1
            else:
                rows[row_string] += 1
        count = 0
        for i in range(len(grid)):
            col_string = []
            for j in range(len(grid)):
                col_string.append(grid[j][i])
            if str(col_string) in rows:
                count += rows[str(col_string)]

        return count
soln = Solution()
print(soln.equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))