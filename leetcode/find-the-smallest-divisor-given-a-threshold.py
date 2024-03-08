class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l, r = 1, max(nums)

        while l <= r:
            mid = (l+r)//2
            _sum = 0
            for num in nums:
                _sum += ceil(num/mid)
            if _sum <= threshold:
                r = mid - 1
            else:
                l = mid + 1
        return l   


        #9 minute         
        