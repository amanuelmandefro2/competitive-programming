class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:   
        ans = []
        def backtrack(path):
            if len(path[:]) == len(nums):
                ans.append(path[:])
                return
            for i in range(len(nums)):
                if nums[i] in path:
                    continue
                path.append(nums[i])
                backtrack(path)
                path.pop()

        backtrack([])            
        return ans        














    #    ans = []
    #     def sub(i, arr):

    #         ans.append(arr[:])
    #         for j in range(i, len(nums)):
    #             arr.append(nums[j])
    #             sub(j+1, arr)
    #             arr.pop()

    #     sub(0, []) 
    #     return ans 
        