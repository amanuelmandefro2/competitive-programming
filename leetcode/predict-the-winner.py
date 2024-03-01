class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        def score(l, r, turn):
            if turn:
                if l == r:
                    return nums[l]
                left = score(l+1, r, not turn) + nums[l]
                right = score(l, r-1, not turn) + nums[r]
                return max(left, right)
            else:
                if l == r:
                    return -nums[l]
                left = score(l+1, r, not turn) - nums[l]
                right = score(l, r-1, not turn) - nums[r]
                return min(left, right)

        return score(0, len(nums)-1, True) >= 0               
