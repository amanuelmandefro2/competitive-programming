class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        max_col,max_row  = [], []
        ans = 0
        for row in grid:
            max_row.append(max(row))
        for c in range(len(grid[0])):
            _max = 0
            for r in range(len(grid)):
                _max = max(_max, grid[r][c])
            max_col.append(_max)        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                ans += min(max_row[r], max_col[c]) - grid[r][c]
        
        return ans    

        