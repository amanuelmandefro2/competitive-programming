class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        curr_sum, _max = 0, 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            _max = max(_max, ceil(curr_sum/(i+1)))


        return _max            
        