class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        ans = [-1]*len(intervals)
        n = len(intervals)
        intervals_pos = []
        for i, interval in enumerate(intervals):
            intervals_pos.append([interval, i])
        intervals_pos.sort()    
        # print(intervals_pos)     
        for i in range(n):
            l, r = 0, n -1
            while l <= r:
                mid = (l+r)//2
                if intervals_pos[mid][0][0] >= intervals[i][1]:
                    ans[i] = intervals_pos[mid][1]  
                    r = mid - 1
                else:
                    l = mid + 1
                  
        return ans                

       