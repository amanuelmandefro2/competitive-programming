class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        sum_marbles = []
        
        for i in range(len(weights)-1):
            sum_marbles.append(weights[i] + weights[i+1])
        sum_marbles.sort()  
        min_score = sum(sum_marbles[:k-1])
        max_score = 0
        for i in range(1, k):
            max_score += sum_marbles[-i]
  
        return max_score - min_score
        