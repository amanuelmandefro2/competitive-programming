class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack, ans = [], [-1]*len(nums)
        
        for i in range(len(nums)*2):
            index = i%len(nums)
            while stack and nums[stack[-1]] < nums[index]:
                ans[stack.pop()] = nums[index]
            stack.append(index)

        return ans            

        