class Solution:
    def totalNQueens(self, n: int) -> int:
        col, l_diag, r_diag = set(), set(), set()
        ans = 0
        def backtrack(r):
            if r == n:
                nonlocal ans 
                ans += 1
                return 
            for c in range(n):
                if c in col or r-c in r_diag or r + c in l_diag:
                    continue
                col.add(c)
                l_diag.add(r+c)
                r_diag.add(r-c)
                backtrack(r+1)
                col.remove(c)
                l_diag.remove(r+c)
                r_diag.remove(r-c)  
        backtrack(0)

        return ans          

