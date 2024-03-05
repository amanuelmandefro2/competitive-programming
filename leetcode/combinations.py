class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtrack(first, path):
            if len(path) == k:
                ans.append(path.copy())
                return
            if first >= n+1:     
                return
            # for num in range(first_num, n+1):
            path.append(first)
            backtrack(first+1, path)
            path.pop()

            backtrack(first+1, path)

        backtrack(1, [])            
        return ans