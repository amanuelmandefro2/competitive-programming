class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        cursum = 0
        for num in nums:
            cursum = max(cursum, 0) + num
            max_sum = max(max_sum, cursum)
        return max_sum 

        