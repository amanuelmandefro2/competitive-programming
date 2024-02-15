class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        N = len(nums)

        if len(set(nums)) == N:
            return [0] * N

        ans = [None] * N
        dct = defaultdict(list)
        for inx in range(N):
            dct[nums[inx]].append(inx)
        
        for k, v in dct.items():
            length = len(v)
            if length == 1:
                ans[v[0]] = 0
            else:
                suffix_sum = sum(v)
                prefix_sum = 0
                for i in range(length):
                    curr = dct[k][i]
                    ans[curr] = (i * curr - prefix_sum) + \
                                (suffix_sum - curr - (length - 1 - i) * curr)
                    suffix_sum -= curr
                    prefix_sum += curr
        
        return ans