class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        path=[] 
        def back(curr):
            if sum(path)==target:
                ans.append(path[:])
                return
            elif sum(path)>target:
                return
            for i in range(curr,len(candidates)):

                path.append(candidates[i])
                back(i)
                path.pop()
        back(0)
        return ans