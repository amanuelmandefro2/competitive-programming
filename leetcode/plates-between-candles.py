class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        prefix, ans = defaultdict(int), [0]*len(queries)
        plate, candle = 0, []
        for i in range(len(s)):
            if s[i] == '|':
                prefix[i] = plate
                candle.append(i)
            else: plate += 1
        if not candle :
            return ans  
        for i in range(len(queries)):
            l, r = queries[i]
            left = bisect_left(candle, l)
            right = bisect_right(candle, r) - 1

            print(left, right)
            print(left, right)
            if left < len(candle) and right < len(candle) and right > -1:
                count = prefix[candle[right]] - prefix[candle[left]]
                ans[i] = max(ans[i], count)
                 
        print(prefix)
        print(candle)        
        
        return ans