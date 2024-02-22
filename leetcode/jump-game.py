class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i, _max = 0, 0
        
        while i < len(nums):
            if _max < i:
                return False   
            _max, i = max(_max, i + nums[i]), i+1

        return True
              
        