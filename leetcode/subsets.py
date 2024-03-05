class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def sub(i, arr):

            ans.append(arr[:])
            for i in range(i, len(nums)):
                arr.append(nums[i])
                sub(i+1, arr)
                arr.pop()

        sub(0, []) 
        return ans



        