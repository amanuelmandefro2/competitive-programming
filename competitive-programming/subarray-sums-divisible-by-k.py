class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        curr_sum = 0
        ans = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            if curr_sum % k in prefix:
                ans += prefix[curr_sum%k]
            prefix[curr_sum%k] += 1

        return ans        



        