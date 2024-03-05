class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        prev_row = self.getRow(rowIndex-1)
        curr_row = [0]*(rowIndex + 1)
        curr_row[0], curr_row[rowIndex] = 1, 1

        for i in range(1, rowIndex): 
            curr_row[i] = prev_row[i-1] + prev_row[i]
            
        return curr_row      

        