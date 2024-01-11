class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        max_score = -float('inf')
        unique_score = set()
        curr_sum = 0
        l = 0
        for i in range(len(nums)):
            while nums[i] in unique_score:
                unique_score.remove(nums[l])
                curr_sum -= nums[l]
                l += 1
            unique_score.add(nums[i])
            curr_sum += nums[i]
            max_score = max(max_score, curr_sum)

        return max_score

        