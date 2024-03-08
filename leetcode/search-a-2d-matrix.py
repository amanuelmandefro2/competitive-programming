class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t, b = 0, len(matrix) -1
        l, r = 0, len(matrix[0])-1

        while t <= b and l<= r:
            mid1, mid2 = (t+b)//2, (l+r)//2
            if matrix[mid1][mid2] == target:
                return True
            if matrix[mid1][0] > target:
                b = mid1 - 1
            elif matrix[mid1][-1] < target:
                t = mid1 + 1
            else:
                if matrix[mid1][mid2] > target:
                    r = mid2 - 1
                elif  matrix[mid1][mid2] < target: 
                    l = mid2 + 1
        return False                


