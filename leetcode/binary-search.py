class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary(l, r):
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            if l > r:
                return -1     
            if nums[mid] < target:
                return binary(mid+1, r)
            else:
                return binary(l, mid-1)
        return binary(0, len(nums)-1)                

        