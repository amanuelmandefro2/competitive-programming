class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            nums[i] = curr_sum
        before = 0
        for i in range(len(nums)):
            if before == nums[-1] - nums[i]:
                return i
            before = nums[i]

        
        return -1            
