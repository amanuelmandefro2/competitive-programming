class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total_sum = sum(nums)
        left_sum = 0
        res = []
        for i in range(n):
            right_sum = total_sum - nums[i] - left_sum
            res.append(i*nums[i]-left_sum + right_sum - (n-i-1)*nums[i])

            left_sum += nums[i]

        return res    
        # n = len(nums)
        # prefix_sum = [0] * n
        # suffix_sum = [0] * n

        # # Calculate prefix sum
        # prefix_sum[0] = nums[0]
        # curr_sum = 0
        # for i in range(n):
        #     curr_sum += nums[i]
        #     prefix_sum[i] = curr_sum

        # # Calculate suffix sum
        # curr_sum = 0
        # for i in range(n - 1, -1, -1):
        #     curr_sum += nums[i]
        #     suffix_sum[i] = curr_sum

        # result = []
        # for i in range(n):
        #     left_sum = i * nums[i] - prefix_sum[i]
        #     right_sum = suffix_sum[i] - (n - i - 1) * nums[i]

        #     # Calculate the total sum of absolute differences
        #     result.append(left_sum + right_sum)

        # return result
