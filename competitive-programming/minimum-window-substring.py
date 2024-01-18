class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        count_t, window = Counter(t), defaultdict(int)
        need, have = len(count_t), 0
        res_idx, min_length = [-1, -1], float('inf')
        l = 0
       
        for r in range(len(s)):
            c = s[r]
            window[c] += 1
            if c in count_t and window[c] == count_t[c]:
                have += 1
            while have == need:
                if r - l + 1 < min_length:
                    min_length = r - l + 1
                    res_idx = [l, r]
                window[s[l]] -= 1
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1

        l, r = res_idx
        return s[l:r+1]   




                  
                

        