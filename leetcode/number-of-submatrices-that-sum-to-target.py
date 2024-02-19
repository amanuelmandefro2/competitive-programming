class Solution:
    def numSubmatrixSumTarget(self, matrix, target):
        row, col = len(matrix), len(matrix[0])
        count = 0
        prefix =  [[0]*(col + 1) for r in range((row + 1))]

        for i in range(1, row+1):
            for j in range (1, col+1):
                prefix[i][j] = (prefix[i-1][j] + 
                prefix[i][j-1] - 
                prefix[i-1][j-1] + 
                matrix[i-1][j-1])

        for r1 in range(1, row + 1):
            for r2 in range(r1, row + 1):
                sum_count = defaultdict(int)
                sum_count[0] = 1 
                curr_sum = 0
                for c in range(1, col + 1):
                    curr_sum = prefix[r2][c] - prefix[r1-1][c]
                    count += sum_count[curr_sum - target]
                    sum_count[curr_sum] = sum_count[curr_sum] + 1
                    
        return count