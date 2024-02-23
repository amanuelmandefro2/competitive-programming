class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        _max = -float('inf')
        for i in range(len(nums)-1, -1, -1):
            while stack and stack[-1] < nums[i]:
                _max = max(stack.pop(), _max)
            stack.append(nums[i])             
            if stack and stack[-1] < _max:
                return True    

        return False          
 