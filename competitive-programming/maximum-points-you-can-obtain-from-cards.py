class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total_pts = sum(cardPoints)
        sum_window = sum(cardPoints[:n-k])
        min_score = sum_window 
        
        for i in range(n-k, n):
            sum_window -= cardPoints[i-n+k]
            sum_window += cardPoints[i]
            min_score = min(min_score, sum_window)

       

        return total_pts - min_score           


        