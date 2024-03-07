class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        pos = [-1,-1]
        l,r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] >= target:
                if nums[mid] == target:
                    pos[0] = mid
                # pos[1] = max(pos[1], mid)
                r = mid-1
            else:
                l = mid+1
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] <= target:
                if nums[mid] == target:
                    pos[1] = mid
                l = mid +1
            else: r = mid -1                 
              
        return pos                    