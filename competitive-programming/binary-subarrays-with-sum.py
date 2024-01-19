class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        curr_sum = 0
        ans = 0
        
        for i in range(len(nums)):
            curr_sum += nums[i]
            if curr_sum - goal in prefix:
                ans += prefix[curr_sum - goal]
            prefix[curr_sum] += 1
        return ans        