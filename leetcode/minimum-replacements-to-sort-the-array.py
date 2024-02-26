class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)-2, -1, -1):
            if nums[i] > nums[i+1]:
                k = ceil(nums[i]/nums[i+1])
                count += k-1
                nums[i] = floor(nums[i]/k)
                
        
        return count
        