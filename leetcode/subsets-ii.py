class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans, subset_count = [], defaultdict(int)
        def sub(i, arr):
            t = tuple(arr[:])
            if t not in subset_count:
                ans.append(arr[:])
                subset_count[t] = 1    
            last_pop = float('inf')
            for j in range(i, len(nums)):
                if last_pop == nums[j]:
                    continue
                arr.append(nums[j])
                sub(j+1, arr)
                arr.pop()

        sub(0, []) 
        return ans        

































        # res = [[]]
        # for i in range(len(nums)):
        #     if [nums[i]] not in res:  
        #         res.append([nums[i]])
        #     j = i + 1
        #     while j < len(nums):
        #         if nums[i:j+1] not in res:
        #             res.append(nums[i:j+1])
        #         if[nums[i], nums[j]] not in res:
        #             res.append([nums[i], nums[j]])    
        #         j += 1
        # return res            