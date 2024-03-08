class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(len(nums)):
            if nums[i]*2  > target:
                break 
            l,r = i, n-1
            while l <= r: 
                mid = (l+r)//2
                if nums[i] + nums[mid] > target:
                    r = mid -1
                else:
                    l = mid + 1
            if l-i:
                ans += 2**(l-i-1)        



        return ans % (10**9 + 7)

        #20 minute