class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 1
        t = len(s) -1
        prefix_suffix = [0]*t

        curr_count = 0
        for i in range(t):
            if s[i] == '0':
               curr_count += 1
            prefix_suffix[i] +=curr_count 
        curr_count = 0     
        for j in range(t, 0, -1):
            if s[j] == '1':
               curr_count +=1
            prefix_suffix[j-1] +=curr_count
       
        return max(prefix_suffix)      
                
















        # max_score = 0
        # for i in range(1, len(s)):
        #     max_score = max(s[:i].count('0')+s[i:].count('1'), max_score)

        # return max_score    
        