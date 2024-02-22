class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        n, ans = len(nums), 0
        for i in range(n-2):
            l, r = i + 1, n - 1
            while l < r :
                if nums[i] < nums[l]+nums[r]:
                    ans += r - l
                    l += 1
                else:    
                    r -= 1
           
                            
        return ans        