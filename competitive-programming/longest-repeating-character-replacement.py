class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        max_length = 0
        max_count = 0
        count_d = {}
        
        for r in range(len(s)):
            count_d[s[r]] = count_d.get(s[r], 0) + 1
            max_count = max(max_count, count_d[s[r]])
            if (r-l+1)-max_count > k:
                count_d[s[l]] -= 1
                l += 1
            max_length = max(max_length, r - l + 1)
        return max_length
        
        