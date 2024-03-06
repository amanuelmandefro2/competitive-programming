class Solution:
    def mySqrt(self, x: int) -> int:
        ans = 0
        l, r = 1, x
        while l <= r:
            mid = (l+r)//2
            if mid * mid > x:
                r = mid-1
            else:
                l = mid+1
                ans = mid
        return ans                 
        