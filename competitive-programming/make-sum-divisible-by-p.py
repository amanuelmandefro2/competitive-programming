class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        curr_sum = sum(nums)
        if curr_sum % p == 0:
            return 0
        if sum(nums) < p:
            return -1
        prefix = 0 
        subs = defaultdict(int)  
        subs[0] = 0
        ans = len(nums) 
        for i in range(len(nums)):
            prefix += nums[i]
            sub = (prefix - curr_sum) % p

            if sub in subs:
                ans = min(ans, (i+1)-subs[sub])
            
            subs[prefix % p] = i+1
        

       
        return ans if ans < len(nums)  else -1  
        