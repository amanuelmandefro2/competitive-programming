class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i, max_idx = 0, 0
        
        while i < len(nums):
            if max_idx < i:
                return False   
            max_idx, i = max(max_idx, i + nums[i]), i+1

        return True
              
        