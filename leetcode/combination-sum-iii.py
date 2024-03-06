class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        def backtrack(i, k, n, path):
            if len(path[:]) == k:
                if sum(path[:]) == n:
                    ans.append(path[:])
                return     
                    
            for j in range(i, 10):
                if sum(path) > n:
                    continue
                path.append(j) 
                backtrack(j+1, k, n, path)
                path.pop()
               

        backtrack(1, k, n, [])

        return ans              
        