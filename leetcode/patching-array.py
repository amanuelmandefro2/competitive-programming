class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        i, patch = 0, 0
        unreachable = 1
        while unreachable <= n:
            if i < len(nums) and nums[i] <= unreachable: 
                unreachable += nums[i]
                i += 1
            else:
                unreachable *= 2
                patch += 1
        return patch           